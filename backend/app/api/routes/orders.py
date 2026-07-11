from fastapi import APIRouter, Request

from app.models.order import Order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/buy")
def buy(order: Order, request: Request):

    broker = request.app.state.engine.broker()

    return broker.send_order(
        order.model_dump()
    )


@router.post("/sell")
def sell(order: Order, request: Request):

    broker = request.app.state.engine.broker()

    return broker.send_order(
        order.model_dump()
    )