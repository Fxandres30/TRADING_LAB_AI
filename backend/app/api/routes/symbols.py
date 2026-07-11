from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/symbols",
    tags=["Symbols"]
)


@router.get("/")
def symbols(request: Request):

    broker = request.app.state.engine.broker()

    return broker.market.symbols()