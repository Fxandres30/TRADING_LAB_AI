from pydantic import BaseModel

from app.models.contracts import ContractType


class Order(BaseModel):

    symbol: str

    amount: float

    duration: int

    contract_type: ContractType

    stop_loss: float | None = None

    take_profit: float | None = None