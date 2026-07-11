from fastapi import APIRouter

router = APIRouter(
    prefix="/strategies",
    tags=["Strategies"]
)


@router.get("/")
def strategies():

    return {
        "strategies": []
    }