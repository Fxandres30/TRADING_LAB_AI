from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/ticks",
    tags=["Ticks"]
)


@router.get("/{symbol}")
def tick(symbol: str, request: Request):

    broker = request.app.state.engine.broker()

    return broker.market.tick(symbol)