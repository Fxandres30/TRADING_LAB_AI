from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def history(request: Request):

    broker = request.app.state.engine.broker()

    return broker.positions.history()