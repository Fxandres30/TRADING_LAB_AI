from pydantic import BaseModel


class BuyRequest(BaseModel):

    symbol: str

    amount: float

    duration: int

    contract_type: str