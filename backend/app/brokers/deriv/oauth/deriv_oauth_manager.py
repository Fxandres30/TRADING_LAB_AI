from .deriv_oauth_client import DerivOAuthClient
from .deriv_oauth_models import (
    DerivOAuthSession,
    DerivOAuthToken,
)


class DerivOAuthManager:

    def __init__(self):

        self.client = DerivOAuthClient()
        self.session = DerivOAuthSession()

    # =====================================================
    # LOGIN URL
    # =====================================================

    def login_url(self):

        return self.client.authorization_url()

    # =====================================================
    # CALLBACK
    # =====================================================

    def authorize(
        self,
        code: str,
        state: str,
    ) -> DerivOAuthToken:

        print()
        print("=" * 80)
        print("🔐 OAUTH MANAGER")
        print("=" * 80)

        print("Intercambiando código por Access Token...")

        data = self.client.exchange_code(

            code=code,

            state=state,

        )

        print()
        print("Respuesta Deriv:")

        for k, v in data.items():

            print(f"{k:20}: {v}")

        token = DerivOAuthToken(

            access_token=data["access_token"],

            token_type=data.get("token_type", "Bearer"),

            expires_in=data.get("expires_in", 0),

            refresh_token=data.get("refresh_token"),

        )

        self.session.connected = True
        self.session.token = token

        print()
        print("=" * 80)
        print("✅ TOKEN GUARDADO")
        print("=" * 80)

        print("Access Token :", token.access_token)
        print("Token Type   :", token.token_type)
        print("Expires      :", token.expires_in)
        print("Refresh      :", token.refresh_token)

        print("=" * 80)

        return token

    # =====================================================
    # ACCESS TOKEN
    # =====================================================

    @property
    def access_token(self):

        return None if self.session.token is None else self.session.token.access_token

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {

            "connected": self.session.connected,

            "has_token": self.session.token is not None,

            "client": "OAuth",

            "access_token": self.access_token is not None,

        }

    # =====================================================
    # LOGOUT
    # =====================================================

    def logout(self):

        print()

        print("🚪 OAuth Logout")

        self.session = DerivOAuthSession()