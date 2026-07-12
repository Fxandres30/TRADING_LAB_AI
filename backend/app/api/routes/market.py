from fastapi import APIRouter, Request, HTTPException
import traceback

router = APIRouter(
    prefix="/market",
    tags=["Market"],
)

# =====================================================
# SYMBOLS
# =====================================================

@router.get("/symbols")
def symbols(request: Request):

    try:

        engine = request.app.state.engine

        return engine.market.get_symbols()

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(

            status_code=500,

            detail=str(e),

        )


# =====================================================
# TICK
# =====================================================

@router.get("/tick/{symbol}")
def tick(

    symbol: str,

    request: Request,

):

    try:

        engine = request.app.state.engine

        return engine.market.get_tick(

            symbol=symbol,

        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(

            status_code=500,

            detail=str(e),

        )


# =====================================================
# HISTORY
# =====================================================

@router.get("/history")
def history(

    symbol: str,

    request: Request,

    timeframe: str = "M15",

    count: int = 500,

):

    try:

        print("\n" + "=" * 80)
        print("📈 MARKET HISTORY")
        print("=" * 80)

        print("SYMBOL    :", symbol)
        print("TIMEFRAME :", timeframe)
        print("COUNT     :", count)

        engine = request.app.state.engine

        analysis = engine.market.analyze(

            symbol=symbol,

            timeframe=timeframe,

            count=count,

        )

        candles = [

            {

                "time": candle.time,

                "open": candle.open,

                "high": candle.high,

                "low": candle.low,

                "close": candle.close,

            }

            for candle in analysis.candles

        ]

        print("Velas:", len(candles))

        return candles

    except Exception as e:

        print("\n❌ ERROR MARKET HISTORY")

        traceback.print_exc()

        raise HTTPException(

            status_code=500,

            detail={

                "error": str(e),

                "type": type(e).__name__,

                "symbol": symbol,

                "timeframe": timeframe,

            },

        )


# =====================================================
# ANALYZE
# =====================================================

@router.get("/analyze/{symbol}")
def analyze(

    symbol: str,

    request: Request,

    timeframe: str = "M15",

    count: int = 500,

):

    try:

        engine = request.app.state.engine

        analysis = engine.market.analyze(

            symbol=symbol,

            timeframe=timeframe,

            count=count,

        )

        return {

            "ok": True,

            "symbol": analysis.symbol,

            "timeframe": timeframe,

            "candles": len(analysis.candles),

            "last_price": analysis.last_price,

            "last_candle": {

                "time": analysis.last_candle.time,

                "open": analysis.last_candle.open,

                "high": analysis.last_candle.high,

                "low": analysis.last_candle.low,

                "close": analysis.last_candle.close,

            },

        }

    except Exception as e:

        print("\n❌ ERROR ANALYZE")

        traceback.print_exc()

        raise HTTPException(

            status_code=500,

            detail=str(e),

        )