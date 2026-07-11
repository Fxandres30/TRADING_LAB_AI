from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/positions",
    tags=["Positions"]
)


@router.get("/")
def positions(request: Request):

    broker = request.app.state.engine.broker()

    return broker.positions.list()