import MetaTrader5 as mt5


TIMEFRAMES = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15,
    "M30": mt5.TIMEFRAME_M30,
    "H1": mt5.TIMEFRAME_H1,
    "H4": mt5.TIMEFRAME_H4,
    "D1": mt5.TIMEFRAME_D1,

    60: mt5.TIMEFRAME_M1,
    300: mt5.TIMEFRAME_M5,
    900: mt5.TIMEFRAME_M15,
    1800: mt5.TIMEFRAME_M30,
    3600: mt5.TIMEFRAME_H1,
    14400: mt5.TIMEFRAME_H4,
    86400: mt5.TIMEFRAME_D1,
}


class MT5Market:

    def __init__(self, client, accounts):

        self.client = client
        self.accounts = accounts

    # =====================================================
    # CANDLES
    # =====================================================

    def get_candles(
        self,
        symbol,
        timeframe,
        count=500,
    ):

        print("=" * 60)
        print("MT5 MARKET")
        print("Symbol    :", symbol)
        print("Timeframe :", timeframe)
        print("Count     :", count)
        print("=" * 60)

        tf = TIMEFRAMES.get(timeframe)

        if tf is None:
            raise Exception(f"Timeframe inválido: {timeframe}")

        candles = self.client.copy_rates(
            symbol=symbol,
            timeframe=tf,
            count=count,
        )

        if candles is None:
            return []

        if len(candles) == 0:
            return []

        if hasattr(candles, "tolist"):
            return candles.tolist()

        return candles

    # =====================================================
    # TICK
    # =====================================================

    def get_tick(self, symbol):

        tick = self.client.tick(symbol)

        if tick is None:
            return None

        return {
            "bid": tick.bid,
            "ask": tick.ask,
            "spread": tick.ask - tick.bid,
        }

    # =====================================================
    # SYMBOLS
    # =====================================================

    def get_symbols(self):

        symbols = self.client.symbols()

        if symbols is None:
            return []

        return [symbol.name for symbol in symbols]