from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/brokers",
    tags=["Broker"]
)


@router.get("/discover")
def discover(request: Request):

    return request.app.state.engine.brokers.discover()