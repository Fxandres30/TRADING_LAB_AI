class DerivOrders:

    def __init__(self, client):

        self.client = client

    # =====================================================
    # PROPUESTA
    # =====================================================

    def proposal(self, order):

        payload = {

            "proposal": 1,

            "amount": order["amount"],

            "basis": "stake",

            "contract_type": order["contract_type"],

            "currency": "USD",

            "duration": order["duration"],

            "duration_unit": "m",

            "symbol": order["symbol"]

        }

        return self.client.request(payload)

    # =====================================================
    # COMPRAR
    # =====================================================

    def send(self, order):

        proposal = self.proposal(order)

        if "error" in proposal:

            return proposal

        proposal_id = proposal["proposal"]["id"]

        payload = {

            "buy": proposal_id,

            "price": order["amount"]

        }

        return self.client.buy(payload)

    # =====================================================
    # VENDER
    # =====================================================

    def sell(self, contract_id):

        return self.client.sell(contract_id)