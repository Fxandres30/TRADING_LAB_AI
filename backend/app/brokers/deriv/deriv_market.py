from app.brokers.deriv.deriv_candles import DerivCandles


class DerivMarket:

    def __init__(self, client):
        self.client = client
        self.candles = DerivCandles(client)

    # ==========================================
    # HISTORIAL DE VELAS
    # ==========================================

    def history(
        self,
        symbol: str,
        timeframe: int,
        count: int = 500,
    ):
        return self.candles.history(
            symbol=symbol,
            timeframe=timeframe,
            count=count,
        )

    # ==========================================
    # ÚLTIMA VELA
    # ==========================================

    def last(
        self,
        symbol: str,
        timeframe: int,
    ):
        return self.candles.last(
            symbol=symbol,
            timeframe=timeframe,
        )