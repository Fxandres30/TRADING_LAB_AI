from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/account",
    tags=["Account"]
)


@router.get("/")
def account(request: Request):

    broker = request.app.state.engine.broker()

    return broker.get_balance()