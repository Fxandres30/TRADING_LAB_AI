from fastapi import APIRouter, Request, HTTPException
import traceback

from app.market.timeframe import TimeFrame

router = APIRouter(
    prefix="/market",
    tags=["Market"],
)


# =====================================================
# SYMBOLS
# =====================================================

@router.get("/symbols")
def symbols(request: Request):

    print("\n" + "=" * 80)
    print("📊 MARKET /symbols")
    print("=" * 80)

    engine = request.app.state.engine

    broker = engine.broker()

    print("Broker:", broker.name)

    print("Estado Broker:")
    print(broker.status())

    broker.connect()

    return broker.market.symbols()


# =====================================================
# TICK
# =====================================================

@router.get("/tick/{symbol}")
def tick(
    symbol: str,
    request: Request,
):

    print("\n" + "=" * 80)
    print("📊 MARKET /tick")
    print("=" * 80)

    print("Symbol:", symbol)

    engine = request.app.state.engine

    broker = engine.broker()

    print("Estado Broker:")
    print(broker.status())

    broker.connect()

    return broker.market.tick(symbol)


# =====================================================
# HISTORY
# =====================================================

@router.get("/history")
def history(

    symbol: str,
    request: Request,
    timeframe: str = "M1",
    count: int = 500,

):

    print("\n" + "=" * 80)
    print("📈 MARKET HISTORY")
    print("=" * 80)

    print("SYMBOL      :", symbol)
    print("TIMEFRAME   :", timeframe)
    print("COUNT       :", count)

    try:

        engine = request.app.state.engine

        print("\nENGINE")
        print("----------------------------------------")
        print("Running:", engine.running)

        broker = engine.broker()

        print("\nBROKER")
        print("----------------------------------------")
        print("Nombre :", broker.name)

        try:

            status = broker.status()

            print("Estado Broker:")

            for k, v in status.items():

                print(f"{k:15}: {v}")

        except Exception as e:

            print("No fue posible obtener broker.status()")
            print(e)

        print("\nIntentando conectar broker...")

        broker.connect()

        print("Broker conectado correctamente.")

        tf = TimeFrame.from_string(timeframe)

        print("\nTIMEFRAME")
        print("----------------------------------------")
        print(tf)
        print("Segundos:", tf.value)

        print("\nSolicitando análisis...")

        analysis = engine.market.analyze(

            broker=broker,

            symbol=symbol,

            timeframe=tf.value,

            count=count,

        )

        print("\nANALYSIS")
        print("----------------------------------------")

        print("Symbol       :", analysis.symbol)
        print("Last Price   :", analysis.last_price)
        print("Velas        :", len(analysis.candles))

        if analysis.candles:

            first = analysis.candles[0]
            last = analysis.candles[-1]

            print("\nPrimera vela")
            print(vars(first))

            print("\nÚltima vela")
            print(vars(last))

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

        print("\nRespuesta enviada:", len(candles), "velas")

        return candles

    except Exception as e:

        print("\n" + "=" * 80)
        print("❌ ERROR MARKET HISTORY")
        print("=" * 80)

        print("Tipo :", type(e).__name__)
        print("Error:", str(e))

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
    timeframe: str = "M1",
    count: int = 500,

):

    print("\n" + "=" * 80)
    print("📊 MARKET ANALYZE")
    print("=" * 80)

    try:

        engine = request.app.state.engine

        broker = engine.broker()

        broker.connect()

        tf = TimeFrame.from_string(timeframe)

        analysis = engine.market.analyze(

            broker=broker,

            symbol=symbol,

            timeframe=tf.value,

            count=count,

        )

        print("Velas:", len(analysis.candles))

        return {

            "ok": True,

            "symbol": analysis.symbol,

            "timeframe": timeframe,

            "seconds": tf.value,

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