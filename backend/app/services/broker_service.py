from app.brokers.deriv.deriv_client import DerivClient


class BrokerService:

    def __init__(self):

        self.client = DerivClient()

        self.connected = False

    def connect(self):

        self.client.connect()

        self.connected = True

        return {
            "ok": True,
            "message": "Broker conectado"
        }

    def disconnect(self):

        self.client.disconnect()

        self.connected = False

        return {
            "ok": True,
            "message": "Broker desconectado"
        }

    def status(self):

        return {

            "broker": "Deriv",

            "connected": self.connected

        }


broker_service = BrokerService()