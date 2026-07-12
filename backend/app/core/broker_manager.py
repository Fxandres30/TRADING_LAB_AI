from app.core.service import Service

from app.core.service import Service
from app.brokers.broker_discovery import BrokerDiscovery
from app.brokers.broker_discovery import BrokerDiscovery


class BrokerManager(Service):

    def __init__(

        self,

        event_bus,

        accounts,

    ):

        super().__init__()

        self.event_bus = event_bus
        self.accounts = accounts

        self.discovery = BrokerDiscovery()

        self.brokers = {}

        self.default = None

        self.load()

        # Descubre cuentas y conecta brokers automáticamente
        self.initialize()

    # =====================================================
    # LOAD
    # =====================================================

    def load(self):

        # MT5
        try:

            from app.brokers.mt5.mt5_broker import MT5Broker

            self.register(MT5Broker(self.accounts))

        except Exception as e:

            print(f"⚠ MT5 no disponible: {e}")

        # Deriv
        try:

            from app.brokers.deriv.deriv_broker import DerivBroker

            self.register(DerivBroker(self.accounts))

        except Exception as e:

            print(f"⚠ Deriv no disponible: {e}")


    # =====================================================
    # INITIALIZE
    # =====================================================

    def initialize(self):

        print("\n🔍 Buscando cuentas de brokers...\n")

        accounts = self.discovery.discover()

        if not accounts:
            print("⚠ No se encontraron cuentas.")
            return

        print(f"✅ {len(accounts)} cuenta(s) encontrada(s)\n")

        for account in accounts:

            self.accounts.add(account)

        print("--------------------------------")
        print("Broker   :", account.broker)
        print("Empresa  :", account.company)
        print("Login    :", account.login)
        print("Servidor :", account.server)
        print("Balance  :", account.balance)
        print("Equity   :", account.equity)
        print("Moneda   :", account.currency)
        print("Nombre   :", account.name)
        print("--------------------------------")
    # =====================================================
    # REGISTER
    # =====================================================

    def register(self, broker):

        key = broker.name.lower()

        self.brokers[key] = broker

        if self.default is None:

            self.default = key

        print(f"✅ Broker registrado -> {broker.name}")

    # =====================================================
    # GET
    # =====================================================

    def get(self, broker=None):

        if broker is None:

            broker = self.default

        if hasattr(broker, "name"):

            return broker

        broker = str(broker).lower()

        if broker not in self.brokers:

            raise Exception(f"Broker '{broker}' no encontrado.")

        return self.brokers[broker]

    # =====================================================
    # DISCOVER
    # =====================================================

    def discover(self):

        return self.discovery.discover()

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {

            name: broker.status()

            for name, broker in self.brokers.items()

        }

    # =====================================================
    # CANDLES
    # =====================================================

    def get_candles(

        self,

        broker=None,

        symbol="EURUSD",

        timeframe="M15",

        count=500,

    ):

        broker = self.get(broker)

        return broker.get_candles(

            symbol=symbol,

            timeframe=timeframe,

            count=count,

        )

    # =====================================================
    # TICK
    # =====================================================

    def get_tick(

        self,

        broker=None,

        symbol="EURUSD",

    ):

        broker = self.get(broker)

        return broker.get_tick(symbol)

    # =====================================================
    # SYMBOLS
    # =====================================================

    def get_symbols(

        self,

        broker=None,

    ):

        return self.get(broker).get_symbols()

    # =====================================================
    # BALANCE
    # =====================================================

    def get_balance(

        self,

        broker=None,

    ):

        return self.get(broker).get_balance()

    # =====================================================
    # ORDERS
    # =====================================================

    def get_orders(

        self,

        broker=None,

    ):

        return self.get(broker).get_orders()

    # =====================================================
    # POSITIONS
    # =====================================================

    def get_positions(

        self,

        broker=None,

    ):

        return self.get(broker).get_positions()

    # =====================================================
    # SEND ORDER
    # =====================================================

    def send_order(

        self,

        broker=None,

        **kwargs,

    ):

        return self.get(broker).send_order(**kwargs)

    # =====================================================
    # CONNECT
    # =====================================================

    def connect(self):

        for broker in self.brokers.values():

            broker.connect()

    # =====================================================
    # DISCONNECT
    # =====================================================

    def disconnect(self):

        for broker in self.brokers.values():

            broker.disconnect()