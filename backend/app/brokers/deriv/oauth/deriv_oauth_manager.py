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

    def authorize(self, code: str):

        data = self.client.exchange_code(code)

        token = DerivOAuthToken(

            access_token=data["access_token"],

            token_type=data.get(
                "token_type",
                "Bearer",
            ),

            expires_in=data.get(
                "expires_in",
                0,
            ),

            refresh_token=data.get(
                "refresh_token",
            ),

        )

        self.session.connected = True
        self.session.token = token

        return token

    # =====================================================
    # ACCESS TOKEN
    # =====================================================

    def token(self):

        if self.session.token:
            return self.session.token.access_token

        return None

    # =====================================================
    # CONECTADO
    # =====================================================

    def connected(self):

        return self.session.connected

    # =====================================================
    # TIENE TOKEN
    # =====================================================

    def has_token(self):

        return self.token() is not None

    # =====================================================
    # CLIENT
    # =====================================================

    def client_name(self):

        return "OAuth"

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {

            "connected": self.connected(),

            "has_token": self.has_token(),

            "client": self.client_name(),

        }

    # =====================================================
    # LOGOUT
    # =====================================================

    def logout(self):

        self.session = DerivOAuthSession()
        