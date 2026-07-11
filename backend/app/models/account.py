from pydantic import BaseModel


class Account(BaseModel):

    login: str

    balance: float

    currency: str

    broker: str