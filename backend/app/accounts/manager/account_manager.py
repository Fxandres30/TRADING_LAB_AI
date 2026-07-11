from ..storage.account_storage import AccountStorage
from ..models.account_model import AccountModel


class AccountManager:

    def __init__(self):

        self.storage = AccountStorage()

    # =======================================
    # CUENTAS
    # =======================================

    def add_account(

        self,

        broker: str,

        account: AccountModel,

    ):

        item = self.storage.get_broker(broker)

        if item is None:

            raise Exception("Broker no existe")

        item.accounts.append(account)

    def accounts(self):

        data = []

        for broker in self.storage.list_brokers():

            data.extend(broker.accounts)

        return data