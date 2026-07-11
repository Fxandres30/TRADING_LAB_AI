from fastapi import APIRouter

# ==========================================================
# HEALTH
# ==========================================================

from app.api.routes.health import router as health_router

# ==========================================================
# ENGINE
# ==========================================================

from app.api.routes.engine import router as engine_router
from app.api.routes.system import router as system_router

# ==========================================================
# BROKER
# ==========================================================

from app.api.routes.broker import router as broker_router
from app.api.routes.account import router as account_router
from app.api.routes.market import router as market_router
from app.api.routes.orders import router as orders_router
from app.api.routes.positions import router as positions_router
from app.api.routes.history import router as history_router
from app.api.routes.symbols import router as symbols_router
from app.api.routes.ticks import router as ticks_router

# ==========================================================
# DERIV OAUTH
# ==========================================================

from app.brokers.deriv.oauth.routes.deriv_oauth_routes import router as deriv_oauth_router

from app.accounts.routes.account_routes import (
    router as account_manager_router,
)


# ==========================================================
# STRATEGIES
# ==========================================================

from app.api.routes.strategies import router as strategies_router
from app.api.routes.strategy import router as strategy_router
from app.api.routes.backtesting import router as backtesting_router

# ==========================================================
# RISK
# ==========================================================

from app.api.routes.risk import router as risk_router

# ==========================================================
# DATABASE
# ==========================================================

from app.api.routes.database import router as database_router

# ==========================================================
# EVENTS
# ==========================================================

from app.api.routes.events import router as events_router


# ==========================================================
# API
# ==========================================================

api_router = APIRouter(
    prefix="/api"
)


# ==========================================================
# HEALTH
# ==========================================================

api_router.include_router(health_router)


# ==========================================================
# ENGINE
# ==========================================================

api_router.include_router(engine_router)
api_router.include_router(system_router)


# ==========================================================
# BROKER
# ==========================================================

api_router.include_router(broker_router)
api_router.include_router(account_router)
api_router.include_router(market_router)
api_router.include_router(orders_router)
api_router.include_router(positions_router)
api_router.include_router(history_router)
api_router.include_router(symbols_router)
api_router.include_router(ticks_router)


# ==========================================================
# DERIV OAUTH
# ==========================================================

api_router.include_router(deriv_oauth_router)
api_router.include_router(account_manager_router)

# ==========================================================
# STRATEGIES
# ==========================================================

api_router.include_router(strategies_router)
api_router.include_router(strategy_router)
api_router.include_router(backtesting_router)


# ==========================================================
# RISK
# ==========================================================

api_router.include_router(risk_router)


# ==========================================================
# DATABASE
# ==========================================================

api_router.include_router(database_router)


# ==========================================================
# EVENTS
# ==========================================================

api_router.include_router(events_router)