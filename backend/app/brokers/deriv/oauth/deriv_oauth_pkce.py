import base64
import hashlib
import secrets


class DerivOAuthPKCE:

    def __init__(self):

        self.code_verifier: str | None = None
        self.code_challenge: str | None = None
        self.state: str | None = None

    # =====================================================
    # GENERAR PKCE
    # =====================================================

    def generate(self):

        verifier = secrets.token_urlsafe(64)

        digest = hashlib.sha256(
            verifier.encode("utf-8")
        ).digest()

        challenge = (
            base64.urlsafe_b64encode(digest)
            .decode("utf-8")
            .rstrip("=")
        )

        state = secrets.token_urlsafe(32)

        self.code_verifier = verifier
        self.code_challenge = challenge
        self.state = state

        return self

    # =====================================================
    # DATA
    # =====================================================

    def data(self):

        return {
            "state": self.state,
            "code_verifier": self.code_verifier,
            "code_challenge": self.code_challenge,
            "code_challenge_method": "S256",
        }

    # =====================================================
    # READY
    # =====================================================

    @property
    def ready(self):

        return (
            self.code_verifier is not None
            and self.code_challenge is not None
            and self.state is not None
        )

    # =====================================================
    # RESET
    # =====================================================

    def clear(self):

        self.code_verifier = None
        self.code_challenge = None
        self.state = None