import psutil
import MetaTrader5 as mt5

from app.accounts.models.account_model import AccountModel


class MT5Scanner:

    def discover(self):

        print("\n==============================")
        print("🔍 INICIANDO MT5 SCANNER")
        print("==============================")

        accounts = []

        for process in psutil.process_iter(["pid", "name", "exe"]):

            try:

                exe = process.info["exe"]

                if not exe:
                    continue

                exe_lower = exe.lower()

                if (
                    "terminal64.exe" not in exe_lower
                    and
                    "terminal.exe" not in exe_lower
                ):
                    continue

                print(f"\n✅ MT5 DETECTADO")
                print(f"PID      : {process.info['pid']}")
                print(f"Ruta     : {exe}")

                mt5.shutdown()

                print("Inicializando...")

                if not mt5.initialize(path=exe):

                    print("❌ Error initialize")
                    print(mt5.last_error())

                    continue

                info = mt5.account_info()

                if info is None:

                    print("❌ account_info() = None")
                    print(mt5.last_error())

                    mt5.shutdown()

                    continue

                account = AccountModel(

    id=f"mt5-{info.server}-{info.login}",

    broker="mt5",

    company=info.company,

    login=str(info.login),

    server=info.server,

    name=info.name,

    type="demo" if "demo" in info.server.lower() else "real",

    currency=info.currency,

    balance=info.balance,

    equity=info.equity,

    path=exe,

    connected=True,

)

                print(f"✅ {info.company}")
                print(f"   Login   : {info.login}")
                print(f"   Servidor: {info.server}")
                print(f"   Balance : {info.balance}")

                accounts.append(account)

                mt5.shutdown()

            except Exception as e:

                print("❌ ERROR")

                print(type(e).__name__)

                print(e)

        print("\n==============================")
        print(f"TOTAL CUENTAS: {len(accounts)}")
        print("==============================")

        return accounts