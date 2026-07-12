from dataclasses import dataclass


@dataclass(slots=True)
class StrategyInstance:

    id: str

    strategy: str

    broker: str

    account: str

    symbol: str

    timeframe: str

    risk: float

    enabled: bool = True

    running: bool = False