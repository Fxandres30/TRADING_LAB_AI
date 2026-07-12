from ..storage.account_storage import AccountStorage
from ..models.account_model import AccountModel


class AccountManager:

    def __init__(self):

        self.storage = AccountStorage()

        self.selected: AccountModel | None = None

    # =======================================
    # ADD ACCOUNT
    # =======================================

    def add_account(

        self,

        broker: str,

        account: AccountModel,

    ):

        item = self.storage.get_broker(broker)

        if item is None:

            raise Exception(f"Broker '{broker}' no existe")

        # Evitar duplicados
        for acc in item.accounts:

            if acc.id == account.id:

                acc.balance = account.balance
                acc.equity = account.equity
                acc.connected = account.connected
                acc.currency = account.currency
                acc.name = account.name

                return acc

        item.accounts.append(account)

        print(f"✅ Cuenta registrada -> {account.login}")

        return account

    # =======================================
    # ALL
    # =======================================

    def accounts(self):

        data = []

        for broker in self.storage.list_brokers():

            data.extend(broker.accounts)

        return data

    # =======================================
    # GET
    # =======================================

    def get(self, account_id: str):

        for account in self.accounts():

            if account.id == account_id:

                return account

        return None

    # =======================================
    # SELECT
    # =======================================

    def select(self, account_id: str):

        for account in self.accounts():

            account.selected = False

            if account.id == account_id:

                account.selected = True

                self.selected = account

                print(f"🟢 Cuenta activa -> {account.login}")

                return account

        raise Exception("Cuenta no encontrada")

    # =======================================
    # CURRENT
    # =======================================

    def current(self):

        return self.selected

    # =======================================
    # TOTAL BALANCE
    # =======================================

    def total_balance(self):

        return sum(

            account.balance

            for account in self.accounts()

        )

    # =======================================
    # TOTAL EQUITY
    # =======================================

    def total_equity(self):

        return sum(

            account.equity

            for account in self.accounts()

        )

    # =======================================
    # CONNECTED
    # =======================================

    def connected(self):

        return [

            a

            for a in self.accounts()

            if a.connected

        ]