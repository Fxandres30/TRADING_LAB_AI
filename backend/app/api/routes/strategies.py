from fastapi import APIRouter

router = APIRouter(
    prefix="/strategies",
    tags=["Strategies"]
)