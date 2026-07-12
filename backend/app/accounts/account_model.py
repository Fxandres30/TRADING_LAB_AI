from dataclasses import dataclass


@dataclass(slots=True)
class AccountModel:

    id: str

    broker: str

    company: str

    login: str

    server: str

    name: str

    type: str

    currency: str

    balance: float = 0.0

    equity: float = 0.0

    path: str = ""

    connected: bool = False

    selected: bool = False

    access_token: str | None = None

    refresh_token: str | None = None