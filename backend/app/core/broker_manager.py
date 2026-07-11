from app.core.service import Service

from app.brokers.deriv.deriv_broker import DerivBroker


class BrokerManager(Service):

    def __init__(

        self,

        event_bus,

        accounts,

    ):

        super().__init__()

        self.event_bus = event_bus

        self.accounts = accounts

        self.brokers = {}

        self.default = None

        self.load()

    # =====================================================
    # LOAD
    # =====================================================

    def load(self):

        self.register(

            DerivBroker(

                self.accounts,

        )

    )

    # =====================================================
    # REGISTER
    # =====================================================

    def register(self, broker):

        self.brokers[broker.name] = broker

        if self.default is None:

            self.default = broker.name

        print(f"✅ Broker registrado -> {broker.name}")

    # =====================================================
    # GET
    # =====================================================

    def get(self, broker=None):

        if broker is None:

            broker = self.default

        if broker not in self.brokers:

            raise Exception(f"Broker '{broker}' no encontrado.")

        return self.brokers[broker]

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {

            name: broker.status()

            for name, broker in self.brokers.items()

        }

    # =====================================================
    # LIST
    # =====================================================

    def list(self):

        return [

            {

                "name": broker.name,

                "connected": broker.status()["connected"],

                "ready": broker.status()["ready"]

            }

            for broker in self.brokers.values()

        ]