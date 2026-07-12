from pydantic import BaseModel


class Account(BaseModel):

    id: str

    broker: str

    company: str

    login: str

    server: str

    name: str

    currency: str

    balance: float

    equity: float

    connected: bool

    selected: bool