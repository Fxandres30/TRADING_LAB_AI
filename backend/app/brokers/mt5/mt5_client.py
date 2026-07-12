import MetaTrader5 as mt5


class MT5Client:

    def __init__(self):
        self.path = None
        self.connected = False

    # ==========================================
    # CONNECT
    # ==========================================

    def connect(self, path: str):

        if self.connected:
            return True

        self.path = path

        if not mt5.initialize(path=path):
            print("❌ Error inicializando MT5:", mt5.last_error())
            return False

        self.connected = True

        print("✅ MT5 conectado")

        return True

    # ==========================================
    # RECONNECT
    # ==========================================

    def reconnect(self):

        if self.path is None:
            return False

        mt5.shutdown()

        self.connected = False

        return self.connect(self.path)

    # ==========================================
    # ENSURE CONNECTION
    # ==========================================

    def ensure_connection(self):

        if self.connected:
            return True

        return self.reconnect()

    # ==========================================
    # DISCONNECT
    # ==========================================

    def disconnect(self):

        mt5.shutdown()

        self.connected = False

    # ==========================================
    # ACCOUNT
    # ==========================================

    def account_info(self):

        if not self.ensure_connection():
            return None

        return mt5.account_info()

    # ==========================================
    # TERMINAL
    # ==========================================

    def terminal_info(self):

        if not self.ensure_connection():
            return None

        return mt5.terminal_info()

    # ==========================================
    # VERSION
    # ==========================================

    def version(self):

        if not self.ensure_connection():
            return None

        return mt5.version()

    # ==========================================
    # COPY RATES
    # ==========================================

    def copy_rates(self, symbol, timeframe, count):

        if not self.ensure_connection():
            print("❌ Sin conexión MT5")
            return None

        print("=" * 60)
        print("COPY RATES")
        print("SYMBOL    :", symbol)
        print("TIMEFRAME :", timeframe)
        print("COUNT     :", count)

        info = mt5.symbol_info(symbol)

        print("SYMBOL INFO:", info)

        if info is None:
            print("❌ El símbolo no existe")
            return None

        if not info.visible:

            print("⚠ Activando símbolo...")

            mt5.symbol_select(symbol, True)

        data = mt5.copy_rates_from_pos(
            symbol,
            timeframe,
            0,
            count,
        )

        print("DATA:", data)
        print("LAST ERROR:", mt5.last_error())

        if data is None:

            print("❌ copy_rates_from_pos devolvió None")

            return None

        print("VELAS:", len(data))
        print("=" * 60)

        return data

    # ==========================================
    # TICK
    # ==========================================

    def tick(self, symbol):

        if not self.ensure_connection():
            return None

        return mt5.symbol_info_tick(symbol)

    # ==========================================
    # SYMBOLS
    # ==========================================

    def symbols(self):

        if not self.ensure_connection():
            return []

        return mt5.symbols_get()

    # ==========================================
    # POSITIONS
    # ==========================================

    def positions(self):

        if not self.ensure_connection():
            return []

        return mt5.positions_get()

    # ==========================================
    # ORDERS
    # ==========================================

    def orders(self):

        if not self.ensure_connection():
            return []

        return mt5.orders_get()

    # ==========================================
    # SEND ORDER
    # ==========================================

    def order_send(self, request):

        if not self.ensure_connection():
            return None

        result = mt5.order_send(request)

        if result is None:
            print("❌ ORDER ERROR:", mt5.last_error())

        return result