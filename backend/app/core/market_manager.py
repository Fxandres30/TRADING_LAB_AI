from app.core.service import Service
from app.market.analysis import MarketAnalysis


class MarketManager(Service):

    def __init__(

        self,

        event_bus,

        broker_manager,

    ):

        super().__init__()

        self.event_bus = event_bus

        self.brokers = broker_manager

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

        symbol="EURUSD",

    ):

        return self.brokers.get_tick(

            broker=broker,

            symbol=symbol,

        )

    # =====================================================
    # SYMBOLS
    # =====================================================

    def get_symbols(

        self,

        broker=None,

    ):

        return self.brokers.get_symbols(

            broker=broker,

        )

    # =====================================================
    # SNAPSHOT
    # =====================================================

    def snapshot(

        self,

        broker=None,

        symbol="EURUSD",

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

        symbol="EURUSD",

        timeframe="M15",

        count=500,

    ):

        candles = self.get_candles(

            broker=broker,

            symbol=symbol,

            timeframe=timeframe,

            count=count,

        )

        if len(candles) == 0:

            raise Exception("No se recibieron velas.")

        return MarketAnalysis(

            symbol=symbol,

            timeframe=str(timeframe),

            candles=candles,

            last_price=candles[-1].close,

            last_candle=candles[-1],

        )