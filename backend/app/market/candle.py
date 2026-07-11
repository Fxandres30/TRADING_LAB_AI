from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Candle:

    time: datetime

    open: float

    high: float

    low: float

    close: float

    volume: float = 0.0

    spread: float = 0.0

    @property
    def bullish(self) -> bool:
        return self.close > self.open

    @property
    def bearish(self) -> bool:
        return self.close < self.open

    @property
    def body(self) -> float:
        return abs(self.close - self.open)

    @property
    def upper_wick(self) -> float:
        return self.high - max(self.open, self.close)

    @property
    def lower_wick(self) -> float:
        return min(self.open, self.close) - self.low

    @property
    def range(self) -> float:
        return self.high - self.low

    @property
    def midpoint(self) -> float:
        return (self.high + self.low) / 2