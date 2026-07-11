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

        data = self.client.exchange_code(
            code=code,
            state=state,
        )

        token = DerivOAuthToken(
            access_token=data["access_token"],
            token_type=data.get("token_type", "Bearer"),
            expires_in=data.get("expires_in", 0),
            refresh_token=data.get("refresh_token"),
        )

        self.session.connected = True
        self.session.token = token

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
        }

    # =====================================================
    # LOGOUT
    # =====================================================

    def logout(self):
        self.session = DerivOAuthSession()