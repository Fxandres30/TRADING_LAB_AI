from dataclasses import dataclass, field

from app.market.candle import Candle


@dataclass(slots=True)
class MarketAnalysis:

    # =====================================================
    # INFORMACIÓN
    # =====================================================

    symbol: str

    timeframe: str

    candles: list[Candle]

    last_price: float

    last_candle: Candle

    # =====================================================
    # ESTRUCTURA DEL MERCADO
    # =====================================================

    trend: str | None = None

    swings: dict = field(default_factory=dict)

    bos: list = field(default_factory=list)

    choch: list = field(default_factory=list)

    mss: list = field(default_factory=list)

    # =====================================================
    # SMART MONEY
    # =====================================================

    order_blocks: list = field(default_factory=list)

    breaker_blocks: list = field(default_factory=list)

    mitigation_blocks: list = field(default_factory=list)

    fvg: list = field(default_factory=list)

    liquidity: list = field(default_factory=list)

    inducement: list = field(default_factory=list)

    equal_highs: list = field(default_factory=list)

    equal_lows: list = field(default_factory=list)

    # =====================================================
    # INDICADORES
    # =====================================================

    indicators: dict = field(default_factory=dict)

    # =====================================================
    # SEÑALES
    # =====================================================

    signals: list = field(default_factory=list)

    # =====================================================
    # METADATOS
    # =====================================================

    metadata: dict = field(default_factory=dict)