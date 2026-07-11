class DerivPositions:

    def __init__(self, client):

        self.client = client

    # ==========================================
    # POSICIONES
    # ==========================================

    def list(self):

        return self.client.request({

            "portfolio": 1

        })

    # ==========================================
    # HISTORIAL
    # ==========================================

    def history(self):

        return self.client.request({

            "profit_table": 1,

            "limit": 50

        })

    # ==========================================
    # CERRAR
    # ==========================================

    def close(self, contract_id):

        return self.client.request({

            "sell": contract_id,

            "price": 0

        })