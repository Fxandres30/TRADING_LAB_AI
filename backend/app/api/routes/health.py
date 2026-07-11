from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
async def home():
    return {
        "name": "Trading Lab AI",
        "version": "2.0.0",
        "status": "ONLINE",
        "developer": "Andres Mercado"
    }


@router.get("/health")
async def health():
    return {
        "server": "OK",
        "api": "RUNNING"
    }