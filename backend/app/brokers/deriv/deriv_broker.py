from app.brokers.base_broker import BaseBroker

from .deriv_client import DerivClient
from .deriv_account import DerivAccount
from .deriv_market import DerivMarket
from .deriv_orders import DerivOrders
from .deriv_positions import DerivPositions


class DerivBroker(BaseBroker):

    def __init__(self, accounts):

        super().__init__("Deriv")

        self.accounts = accounts

        self.client = DerivClient()

        self.account = DerivAccount(self.client)
        self.market = DerivMarket(self.client)
        self.orders = DerivOrders(self.client)
        self.positions = DerivPositions(self.client)

        self.ready = False

    # =====================================================
    # CONECTAR
    # =====================================================

    def connect(self):

        print()
        print("=" * 60)
        print("🚀 DERIV BROKER")
        print("=" * 60)

        if (
            self.client.is_connected()
            and self.client.is_authorized()
            and self.ready
        ):
            return {
                "ok": True,
                "message": "Broker listo",
            }

        if (
            self.client.is_connected()
            and not self.client.is_authorized()
        ):
            self.client.disconnect()

        self.client.connect()

        # ==========================================
        # CUENTA SELECCIONADA
        # ==========================================

        account = self.accounts.selected()

        if account is None:

            self.client.disconnect()

            raise Exception(
                "No hay una cuenta seleccionada."
            )

        if account.broker != self.name:

            self.client.disconnect()

            raise Exception(
                "La cuenta seleccionada no pertenece a Deriv."
            )

        token = account.access_token

        if not token:

            self.client.disconnect()

            raise Exception(
                "La cuenta no tiene Access Token."
            )

        # ==========================================
        # AUTORIZAR
        # ==========================================

        response = self.client.authorize(token)

        if "error" in response:

            self.client.disconnect()

            raise Exception(
                response["error"]["message"]
            )

        self.ready = True

        return response

    # =====================================================
    # DESCONECTAR
    # =====================================================

    def disconnect(self):

        self.ready = False

        self.client.disconnect()

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        account = self.accounts.selected()

        return {

            "broker": self.name,

            "ready": self.ready,

            "connected": self.client.is_connected(),

            "authorized": self.client.is_authorized(),

            "account": None if account is None else {

                "id": account.id,

                "name": account.name,

                "login": account.login,

                "connected": account.connected,

            }

        }

    # =====================================================
    # CUENTA
    # =====================================================

    def get_balance(self):

        return self.account.balance()

    # =====================================================
    # MERCADO
    # =====================================================

    def get_candles(
        self,
        symbol,
        timeframe,
        count,
    ):

        return self.market.candles(
            symbol,
            timeframe,
            count,
        )

    # =====================================================
    # ORDENES
    # =====================================================

    def send_order(self, order):

        return self.orders.send(order)