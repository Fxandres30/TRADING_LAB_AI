from app.brokers.base_broker import BaseBroker

from .mt5_client import MT5Client
from .mt5_scanner import MT5Scanner
from .mt5_market import MT5Market
from .mt5_orders import MT5Orders
from .mt5_positions import MT5Positions
from .mt5_account import MT5Account


class MT5Broker(BaseBroker):

    def __init__(self, accounts):

        super().__init__("MT5")

        self.accounts = accounts

        # Cliente MT5
        self.client = MT5Client()

        # Scanner
        self.scanner = MT5Scanner()

        # Módulos
        self.market = MT5Market(
            self.client,
            self.accounts,
        )

        self.orders = MT5Orders(
            self.client,
            self.accounts,
        )

        self.positions = MT5Positions(
            self.client,
            self.accounts,
        )

        self.account = MT5Account(
            self.client,
            self.accounts,
        )

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        account = self.accounts.selected()

        return {

            "name": self.name,

            "connected": self.connected,

            "ready": True,

            "selected": account.id if account else None,

        }

    # =====================================================
    # CONNECT
    # =====================================================

    def connect(self):

        account = self.accounts.selected()

        if account is None:
            raise Exception("No hay una cuenta MT5 seleccionada.")

        ok = self.client.connect(account.path)

        self.connected = ok

        return ok

    # =====================================================
    # DISCONNECT
    # =====================================================

    def disconnect(self):

        self.client.disconnect()

        self.connected = False

    # =====================================================
    # DISCOVER
    # =====================================================

    def discover(self):

        return self.scanner.discover()

    # =====================================================
    # ACCOUNT
    # =====================================================

    def get_account(self):

        return self.account.get_account()

    # =====================================================
    # BALANCE
    # =====================================================

    def get_balance(self):

        return self.account.get_balance()

    # =====================================================
    # MARKET
    # =====================================================

    def get_candles(self, symbol, timeframe, count=500):

        return self.market.get_candles(
            symbol,
            timeframe,
            count,
        )

    def get_tick(self, symbol):

        return self.market.get_tick(symbol)



        return self.market.get_symbols()

    # =====================================================
    # POSITIONS
    # =====================================================

    def get_positions(self):

        return self.positions.get_positions()

    # =====================================================
    # ORDERS
    # =====================================================

    def get_orders(self):

        return self.orders.get_orders()

    # =====================================================
    # SEND ORDER
    # =====================================================

    def send_order(self, **kwargs):

        return self.orders.send_order(**kwargs)

    # =====================================================
    # CLOSE POSITION
    # =====================================================

    def close_position(self, ticket):

        return self.positions.close(ticket)