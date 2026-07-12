class MT5Orders:

    def __init__(

        self,

        client,

        accounts,

    ):

        self.client = client
        self.accounts = accounts

    # =====================================================
    # ORDERS
    # =====================================================

    def get_orders(self):

        orders = self.client.orders()

        if orders is None:
            return []

        return list(orders)

    # =====================================================
    # SEND ORDER
    # =====================================================

    def send_order(

        self,

        **kwargs,

    ):

        return self.client.order_send(kwargs)