class MT5Account:

    def __init__(

        self,

        client,

        accounts,

    ):

        self.client = client
        self.accounts = accounts

    # ==========================================
    # ACCOUNT
    # ==========================================

    def get_account(self):

        return self.client.account_info()

    # ==========================================
    # BALANCE
    # ==========================================

    def get_balance(self):

        info = self.client.account_info()

        if info is None:
            return 0.0

        return info.balance

    # ==========================================
    # EQUITY
    # ==========================================

    def get_equity(self):

        info = self.client.account_info()

        if info is None:
            return 0.0

        return info.equity