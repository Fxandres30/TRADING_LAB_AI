from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/system",
    tags=["System"]
)


@router.get("/status")
def status(request: Request):

    return request.app.state.engine.status()