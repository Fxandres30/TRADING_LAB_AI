from app.market.candle import Candle


class SwingDetector:

    def detect(self, candles: list[Candle], left=2, right=2):

        highs = []
        lows = []

        total = len(candles)

        for i in range(left, total - right):

            candle = candles[i]

            # ===========================
            # SWING HIGH
            # ===========================

            if all(
                candle.high > candles[j].high
                for j in range(i - left, i)
            ) and all(
                candle.high > candles[j].high
                for j in range(i + 1, i + right + 1)
            ):

                highs.append({
                    "index": i,
                    "price": candle.high,
                    "time": candle.time,
                })

            # ===========================
            # SWING LOW
            # ===========================

            if all(
                candle.low < candles[j].low
                for j in range(i - left, i)
            ) and all(
                candle.low < candles[j].low
                for j in range(i + 1, i + right + 1)
            ):

                lows.append({
                    "index": i,
                    "price": candle.low,
                    "time": candle.time,
                })

        return {

            "highs": highs,

            "lows": lows,

        }