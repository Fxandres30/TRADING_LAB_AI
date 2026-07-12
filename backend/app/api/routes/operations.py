from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

@router.get("/stats")
def stats(request: Request):

    broker = request.app.state.engine.broker()

    operaciones = broker.history.list()   # o la función que ya tengas

    ganadas = sum(1 for o in operaciones if o["profit"] > 0)
    perdidas = sum(1 for o in operaciones if o["profit"] < 0)
    profit = sum(o["profit"] for o in operaciones)

    account = broker.account.info()

    return {
        "operaciones": len(operaciones),
        "ganadas": ganadas,
        "perdidas": perdidas,
        "profit": profit,
        "balance": account["balance"],
        "equity": account["equity"],
    }