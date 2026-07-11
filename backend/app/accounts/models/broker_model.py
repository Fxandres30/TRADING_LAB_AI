from dataclasses import dataclass, field

from .account_model import AccountModel


@dataclass
class BrokerModel:

    id: str

    name: str

    icon: str = ""

    connected: bool = False

    accounts: list[AccountModel] = field(default_factory=list)