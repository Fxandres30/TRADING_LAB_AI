from app.brokers.deriv.deriv_candles import DerivCandles


class DerivMarket:

    def __init__(self, client):

        self.client = client

        self.candles_service = DerivCandles(client)

    # ==========================================
    # HISTORIAL
    # ==========================================

    def candles(

        self,

        symbol: str,

        timeframe: int,

        count: int = 500,

    ):

        return self.candles_service.history(

            symbol=symbol,

            timeframe=timeframe,

            count=count,

        )

    # ==========================================
    # ÚLTIMA VELA
    # ==========================================

    def last_candle(

        self,

        symbol: str,

        timeframe: int,

    ):

        return self.candles_service.last(

            symbol=symbol,

            timeframe=timeframe,

        )