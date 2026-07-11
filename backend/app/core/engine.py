from app.core.event_bus import EventBus

from app.core.broker_manager import BrokerManager
from app.core.market_manager import MarketManager
from app.core.strategy_manager import StrategyManager
from app.core.risk_manager import RiskManager
from app.core.execution_manager import ExecutionManager
from app.core.database_manager import DatabaseManager
from app.accounts.account_manager import AccountManager

class TradingEngine:

    def __init__(self):

        self.running = False

        self.events = EventBus()

        # ==========================================
        # CUENTAS
        # ==========================================

        self.accounts = AccountManager()

        # ==========================================
        # BROKERS
        # ==========================================

        self.brokers = BrokerManager(

            self.events,

            self.accounts,

        )

        self.market = MarketManager(

            self.events,

            self.brokers,

        )

        self.strategies = StrategyManager(self.events)

        self.risk = RiskManager(self.events)

        self.execution = ExecutionManager(self.events)

        self.database = DatabaseManager(self.events)
        
    # =====================================================
    # START
    # =====================================================

    def start(self):

        if self.running:
            return

        print()
        print("=" * 60)
        print("⚙ INICIALIZANDO ENGINE")
        print("=" * 60)

        self.running = True

        self.brokers.start()
        self.market.start()
        self.strategies.start()
        self.risk.start()
        self.execution.start()
        self.database.start()

        print()
        print("🟢 ENGINE INICIADO")

    # =====================================================
    # STOP
    # =====================================================

    def stop(self):

        if not self.running:
            return

        print()
        print("=" * 60)
        print("🛑 DETENIENDO ENGINE")
        print("=" * 60)

        self.execution.stop()
        self.risk.stop()
        self.strategies.stop()
        self.market.stop()
        self.database.stop()

        self.brokers.disconnect()

        self.brokers.stop()

        self.running = False

        print("🔴 ENGINE DETENIDO")

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {

            "running": self.running,

            "brokers": self.brokers.status(),

            "market": self.market.running,

            "strategies": self.strategies.running,

            "risk": self.risk.running,

            "execution": self.execution.running,

            "database": self.database.running

        }

    # =====================================================
    # BROKER
    # =====================================================

    def broker(self):

        return self.brokers.get()

    # =====================================================
    # EVENTS
    # =====================================================

    def emit(self, event, data=None):

        self.events.emit(event, data)