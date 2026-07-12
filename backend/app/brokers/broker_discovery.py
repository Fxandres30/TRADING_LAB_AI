class BrokerDiscovery:

    def __init__(self):

        print("🚀 BrokerDiscovery creado")

        self.mt5 = None

        try:

            from app.brokers.mt5.mt5_scanner import MT5Scanner

            self.mt5 = MT5Scanner()

            print("✅ MT5 Scanner disponible")

        except Exception as e:

            print(f"⚠ MT5 Scanner no disponible: {e}")

    def discover(self):

        print("\n==============================")
        print("🔍 BrokerDiscovery.discover()")
        print("==============================")

        accounts = []

        if self.mt5 is not None:

            try:

                print("➡ Ejecutando MT5Scanner...")

                mt5_accounts = self.mt5.discover()

                print(f"✅ MT5Scanner devolvió {len(mt5_accounts)} cuentas")

                accounts.extend(mt5_accounts)

            except Exception as e:

                print("❌ ERROR BrokerDiscovery")
                print(type(e).__name__)
                print(e)

        else:

            print("ℹ MT5 Scanner omitido.")

        print("📦 Resultado final:")
        print(accounts)
        print("==============================\n")

        return accounts