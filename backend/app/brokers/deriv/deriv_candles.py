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

        # Error devuelto por Deriv
        if isinstance(response, dict) and "error" in response:

            error = response["error"]

            if isinstance(error, dict):
                message = error.get("message", "Error desconocido")
            else:
                message = str(error)

            raise Exception(message)

        # Sin datos
        if not response or "candles" not in response:
            return []

        candles = []

        for item in response["candles"]:
            candles.append(
                Candle(
                    time=datetime.fromtimestamp(int(item["epoch"])),
                    open=float(item["open"]),
                    high=float(item["high"]),
                    low=float(item["low"]),
                    close=float(item["close"]),
                    volume=float(item.get("volume", 0)),
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

        return candles[0] if candles else None