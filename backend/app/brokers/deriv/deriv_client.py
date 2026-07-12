from .deriv_websocket import DerivWebSocket


class DerivClient:

    def __init__(self):
        self.ws = DerivWebSocket()
        self.authorized = None

    # =====================================================
    # CONEXIÓN
    # =====================================================

    def connect(self):

        if self.ws.is_connected():
            return

        print("🔌 Conectando con Deriv...")

        self.ws.connect()

        print("✅ WebSocket conectado")

    def disconnect(self):

        if self.ws.is_connected():
            self.ws.disconnect()

        self.clear_session()

    def is_connected(self):
        return self.ws.is_connected()

    # =====================================================
    # SESIÓN
    # =====================================================

    def is_authorized(self):
        return self.authorized is not None

    def clear_session(self):
        self.authorized = None

    def require_authorized(self):

        if not self.is_authorized():
            raise Exception(
                "No hay una cuenta Deriv autorizada."
            )

    # =====================================================
    # REQUEST
    # =====================================================

    def request(self, payload):

        if not self.is_connected():
            self.connect()

        self.ws.send(payload)

        response = self.ws.receive()

        if response is None:
            raise Exception("Deriv no respondió.")

        if "error" in response:
            raise Exception(
                response["error"].get(
                    "message",
                    "Error desconocido."
                )
            )

        return response

    # =====================================================
    # AUTH
    # =====================================================

    def authorize(self, token):

        response = self.request({
            "authorize": token
        })

        self.authorized = response.get("authorize")

        return response

    # =====================================================
    # PING
    # =====================================================

    def ping(self):
        return self.request({
            "ping": 1
        })

    # =====================================================
    # CUENTA
    # =====================================================

    def profile(self):

        self.require_authorized()

        return self.authorized

    def balance(self):

        self.require_authorized()

        return self.request({
            "balance": 1
        })

    # =====================================================
    # MERCADO
    # =====================================================

    def active_symbols(self):

        return self.request({
            "active_symbols": "brief"
        })

    def tick(self, symbol):

        return self.request({
            "ticks": symbol,
            "subscribe": 0
        })

    def candles(
        self,
        symbol,
        granularity,
        count=500,
    ):

        self.require_authorized()

        return self.request({
            "ticks_history": symbol,
            "style": "candles",
            "granularity": granularity,
            "count": count,
            "end": "latest",
        })

    # =====================================================
    # PORTAFOLIO
    # =====================================================

    def portfolio(self):

        self.require_authorized()

        return self.request({
            "portfolio": 1
        })

    def history(self):

        self.require_authorized()

        return self.request({
            "profit_table": 1,
            "limit": 50
        })

    # =====================================================
    # ÓRDENES
    # =====================================================

    def buy(self, payload):

        self.require_authorized()

        return self.request(payload)

    def sell(self, contract_id):

        self.require_authorized()

        return self.request({
            "sell": contract_id,
            "price": 0
        })
    
    # =====================================================
# LOGIN
# =====================================================

def login(self):

    self.require_authorized()

    return self.authorized.get("loginid")


def fullname(self):

    self.require_authorized()

    return self.authorized.get("fullname", "")


def currency(self):

    self.require_authorized()

    return self.authorized.get("currency", "")


def balance_value(self):

    self.require_authorized()

    return self.authorized.get("balance", 0)