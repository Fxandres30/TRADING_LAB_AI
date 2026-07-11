from datetime import datetime

from app.market.candle import Candle


class DerivCandles:

    def __init__(self, client):

        self.client = client

    # ==========================================
    # HISTORIAL DE VELAS
    # ==========================================

    def history(

        self,

        symbol: str,

        timeframe: int,

        count: int = 500,

    ) -> list[Candle]:

        response = self.client.candles(

            symbol=symbol,

            granularity=timeframe,

            count=count,

        )

        if "error" in response:

            raise Exception(response["error"])

        if "candles" not in response:

            return []

        candles = []

        for item in response["candles"]:

            candles.append(

                Candle(

                    time=datetime.fromtimestamp(

                        int(item["epoch"])

                    ),

                    open=float(item["open"]),

                    high=float(item["high"]),

                    low=float(item["low"]),

                    close=float(item["close"]),

                    volume=float(

                        item.get("volume", 0)

                    ),

                )

            )

        return candles

    # ==========================================
    # ÚLTIMA VELA
    # ==========================================

    def last(

        self,

        symbol: str,

        timeframe: int,

    ) -> Candle | None:

        candles = self.history(

            symbol=symbol,

            timeframe=timeframe,

            count=1,

        )

        if not candles:

            return None

        return candles[0]