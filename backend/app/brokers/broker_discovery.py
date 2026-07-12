from app.brokers.mt5.mt5_scanner import MT5Scanner


class BrokerDiscovery:

    def __init__(self):

        print("🚀 BrokerDiscovery creado")

        self.mt5 = MT5Scanner()

    def discover(self):

        print("\n==============================")
        print("🔍 BrokerDiscovery.discover()")
        print("==============================")

        accounts = []

        try:

            print("➡ Ejecutando MT5Scanner...")

            mt5_accounts = self.mt5.discover()

            print(f"✅ MT5Scanner devolvió {len(mt5_accounts)} cuentas")

            accounts.extend(mt5_accounts)

        except Exception as e:

            print("❌ ERROR BrokerDiscovery")
            print(type(e).__name__)
            print(e)

        print("📦 Resultado final:")

        print(accounts)

        print("==============================\n")

        return accounts