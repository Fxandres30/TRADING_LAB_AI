import json
import websocket

from app.config.settings import settings


class DerivWebSocket:

    def __init__(self):

        self.ws = None

        self.url = (
            f"wss://ws.derivws.com/websockets/v3"
            f"?app_id={settings.DERIV_APP_ID}"
        )

    # ============================================
    # CONEXIÓN
    # ============================================

    def connect(self):

        if self.is_connected():

            print("🟡 WebSocket ya conectado")

            return

        print()
        print("=" * 60)
        print("🌐 CONECTANDO WEBSOCKET")
        print("=" * 60)

        print("URL:")
        print(self.url)

        try:

            self.ws = websocket.create_connection(
                self.url,
                timeout=10
            )

            print("🟢 WebSocket conectado")

        except Exception as e:

            self.ws = None

            print("🔴 Error WebSocket")
            print(e)

            raise

    # ============================================
    # DESCONECTAR
    # ============================================

    def disconnect(self):

        if not self.ws:
            return

        self.ws.close()

        self.ws = None

        print("🔴 WebSocket desconectado")

    # ============================================
    # ENVIAR
    # ============================================

    def send(self, payload):

        if not self.is_connected():
            raise Exception("WebSocket no conectado")

        print("📤", payload)

        self.ws.send(json.dumps(payload))

    # ============================================
    # RECIBIR
    # ============================================

    def receive(self):

        if not self.is_connected():
            raise Exception("WebSocket no conectado")

        response = json.loads(self.ws.recv())

        print("📥", response)

        return response

    # ============================================
    # ESTADO
    # ============================================

    def is_connected(self):

        return self.ws is not None