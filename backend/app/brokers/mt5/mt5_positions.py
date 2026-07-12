class MT5Positions:

    def __init__(

        self,

        client,

        accounts,

    ):

        self.client = client
        self.accounts = accounts

    # =====================================================
    # POSITIONS
    # =====================================================

    def get_positions(self):

        positions = self.client.positions()

        if positions is None:
            return []

        return list(positions)

    # =====================================================
    # CLOSE
    # =====================================================

    def close(

        self,

        ticket,

    ):

        raise NotImplementedError("Próximamente")