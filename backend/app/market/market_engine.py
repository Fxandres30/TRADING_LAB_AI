from app.core.broker_manager import BrokerManager
from app.market.timeframe import TimeFrame


class MarketEngine:

    def __init__(self):
        self.brokers = BrokerManager()

    def get_candles(
        self,
        broker: str,
        symbol: str,
        timeframe: TimeFrame,
        count: int = 500,
    ):

        broker_instance = self.brokers.get(broker)

        return broker_instance.get_candles(
            symbol=symbol,
            timeframe=tf.value,
            count=count,
        )