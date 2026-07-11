from ..models.broker_model import BrokerModel


class AccountStorage:

    def __init__(self):

        self.brokers: dict[str, BrokerModel] = {}

    # =======================================
    # BROKER
    # =======================================

    def add_broker(self, broker: BrokerModel):

        self.brokers[broker.id] = broker

    def get_broker(self, broker: str):

        return self.brokers.get(broker)

    def list_brokers(self):

        return list(self.brokers.values())