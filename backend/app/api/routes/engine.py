from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/engine",
    tags=["Engine"]
)


@router.get("/status")
async def status(request: Request):

    engine = request.app.state.engine

    return {
        "running": engine.running,
        "brokers": engine.brokers.list()
    }