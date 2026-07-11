from .account_model import AccountModel


class AccountManager:

    def __init__(self):

        self.accounts = {}

    # =====================================================
    # AGREGAR
    # =====================================================

    def add(self, account: AccountModel):

        self.accounts[account.id] = account

    # =====================================================
    # OBTENER
    # =====================================================

    def get(self, account_id):

        return self.accounts.get(account_id)

    # =====================================================
    # TODAS
    # =====================================================

    def all(self):

        return list(self.accounts.values())

    # =====================================================
    # SELECCIONADA
    # =====================================================

    def selected(self):

        for account in self.accounts.values():

            if account.selected:

                return account

        return None

    # =====================================================
    # SELECCIONAR
    # =====================================================

    def select(self, account_id):

        for account in self.accounts.values():

            account.selected = False

        if account_id in self.accounts:

            self.accounts[account_id].selected = True

    # =====================================================
    # ELIMINAR
    # =====================================================

    def remove(self, account_id):

        if account_id in self.accounts:

            del self.accounts[account_id]