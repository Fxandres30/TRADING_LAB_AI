from fastapi import APIRouter

router = APIRouter(
    prefix="/database",
    tags=["Database"]
)


@router.get("/")
def database():

    return {
        "status": "ok"
    }