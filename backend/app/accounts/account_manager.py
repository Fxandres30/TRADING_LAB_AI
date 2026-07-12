from .account_model import AccountModel


class AccountManager:

    def __init__(self):
        self.accounts: dict[str, AccountModel] = {}

    # =====================================================
    # AGREGAR / ACTUALIZAR
    # =====================================================

    def add(self, account: AccountModel):
        self.accounts[account.id] = account
        return account

    # =====================================================
    # OBTENER
    # =====================================================

    def get(self, account_id: str):
        return self.accounts.get(account_id)

    # =====================================================
    # TODAS
    # =====================================================

    def all(self):
        return list(self.accounts.values())

    # =====================================================
    # EXISTE
    # =====================================================

    def exists(self, account_id: str):
        return account_id in self.accounts

    # =====================================================
    # CUENTA SELECCIONADA
    # =====================================================

    def selected(self):

        for account in self.accounts.values():

            if account.selected:
                return account

        return None

    # =====================================================
    # HAY CUENTA SELECCIONADA
    # =====================================================

    def has_selected(self):
        return self.selected() is not None

    # =====================================================
    # SELECCIONAR
    # =====================================================

    def select(self, account_id: str):

        for account in self.accounts.values():
            account.selected = False

        account = self.get(account_id)

        if account is None:
            raise Exception(f"La cuenta '{account_id}' no existe.")

        account.selected = True

        return account

    # =====================================================
    # DESELECCIONAR TODAS
    # =====================================================

    def clear_selection(self):

        for account in self.accounts.values():
            account.selected = False

    # =====================================================
    # ELIMINAR
    # =====================================================

    def remove(self, account_id: str):

        if account_id in self.accounts:
            del self.accounts[account_id]

    # =====================================================
    # LIMPIAR
    # =====================================================

    def clear(self):
        self.accounts.clear()

        # =====================================================
    # BALANCE TOTAL
    # =====================================================

    def total_balance(self):

        return sum(account.balance for account in self.accounts.values())

    # =====================================================
    # EQUITY TOTAL
    # =====================================================

    def total_equity(self):

        return sum(account.equity for account in self.accounts.values())

    # =====================================================
    # TOTAL CUENTAS
    # =====================================================

    def count(self):

        return len(self.accounts)