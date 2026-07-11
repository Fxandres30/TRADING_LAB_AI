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

        print("🔌 Abriendo conexión...")

        self.ws.connect()

        print("✅ Conexión establecida")

    def disconnect(self):

        if not self.ws.is_connected():
            return

        print("🔌 Cerrando conexión...")

        self.ws.disconnect()

        self.clear_session()

    def is_connected(self):

        return self.ws.is_connected()

    # =====================================================
    # AUTH
    # =====================================================

    def is_authorized(self):

        return self.authorized is not None

    def clear_session(self):

        self.authorized = None

    # =====================================================
    # MENSAJES
    # =====================================================

    def send(self, payload):

        self.ws.send(payload)

    def receive(self):

        return self.ws.receive()

    def request(self, payload):

        if not self.is_connected():

            self.connect()

        self.send(payload)

        return self.receive()

    # =====================================================
    # AUTORIZACIÓN
    # =====================================================

    def authorize(self, token):

        response = self.request({

            "authorize": token

        })

        if "authorize" in response:

            self.authorized = response["authorize"]

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

    def balance(self):

        return self.request({

            "balance": 1

        })

    def profile(self):

        return self.authorized

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

        count,

    ):

        return self.request({

            "ticks_history": symbol,

            "style": "candles",

            "granularity": granularity,

            "count": count,

            "end": "latest",

        })

    # =====================================================
    # POSICIONES
    # =====================================================

    def portfolio(self):

        return self.request({

            "portfolio": 1

        })

    def history(self):

        return self.request({

            "profit_table": 1,

            "limit": 50

        })

    # =====================================================
    # ÓRDENES
    # =====================================================

    def buy(self, payload):

        return self.request(payload)

    def sell(self, contract_id):

        return self.request({

            "sell": contract_id,

            "price": 0

        })