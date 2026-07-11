from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.config.settings import settings
from app.core.engine import TradingEngine
from fastapi.middleware.cors import CORSMiddleware


# ======================================================
# ENGINE
# ======================================================

engine = TradingEngine()


# ======================================================
# LIFECYCLE
# ======================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    print()
    print("=" * 60)
    print("🚀 Iniciando Trading Lab AI")
    print("=" * 60)

    engine.start()

    yield

    print()
    print("=" * 60)
    print("🛑 Cerrando Trading Lab AI")
    print("=" * 60)

    engine.stop()


# ======================================================
# APP
# ======================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    lifespan=lifespan,
)

# ======================================================
# CORS
# ======================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================================================
# STATE
# ======================================================

app.state.engine = engine


# ======================================================
# ROUTERS
# ======================================================

app.include_router(api_router)