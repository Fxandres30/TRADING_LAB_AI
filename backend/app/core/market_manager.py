from app.core.service import Service
from app.market.analysis import MarketAnalysis


class MarketManager(Service):

    def __init__(self, event_bus, broker_manager):

        super().__init__()

        self.event_bus = event_bus
        self.brokers = broker_manager

    # =====================================================
    # CANDLES
    # =====================================================

    def get_candles(
        self,
        broker=None,
        symbol="frxEURUSD",
        timeframe=60,
        count=500,
    ):

        print("=" * 60)
        print(type(self.brokers))
        print(dir(self.brokers))
        print("=" * 60)

        return self.brokers.get_candles(
            broker=broker,
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
        symbol="frxEURUSD",
    ):

        instance = self.brokers.connect(broker)

        return instance.market.tick(symbol)

    # =====================================================
    # SNAPSHOT
    # =====================================================

    def snapshot(
        self,
        broker=None,
        symbol="frxEURUSD",
    ):

        return {
            "tick": self.get_tick(
                broker=broker,
                symbol=symbol,
            )
        }

    # =====================================================
    # ANALYZE
    # =====================================================

    def analyze(
        self,
        broker=None,
        symbol="frxEURUSD",
        timeframe=60,
        count=500,
    ):

        candles = self.get_candles(
            broker=broker,
            symbol=symbol,
            timeframe=timeframe,
            count=count,
        )

        if not candles:
            raise Exception("No se recibieron velas")

        return MarketAnalysis(
            symbol=symbol,
            timeframe=str(timeframe),
            candles=candles,
            last_price=candles[-1].close,
            last_candle=candles[-1],
        )