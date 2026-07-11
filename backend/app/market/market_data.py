from abc import ABC, abstractmethod

from .candle import Candle


class MarketDataProvider(ABC):

    @abstractmethod
    async def get_candles(
        self,
        symbol: str,
        timeframe: str,
        count: int,
    ) -> list[Candle]:
        pass
    