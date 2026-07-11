from fastapi import APIRouter

router = APIRouter(
    prefix="/risk",
    tags=["Risk"]
)


@router.get("/")
def risk():

    return {
        "status": "ok"
    }