import base64
import hashlib
import secrets


class DerivOAuthPKCE:

    def __init__(self):

        self.code_verifier = ""

        self.code_challenge = ""

        self.state = ""

    # =====================================================
    # GENERAR
    # =====================================================

    def generate(self):

        self.code_verifier = secrets.token_urlsafe(64)

        digest = hashlib.sha256(
            self.code_verifier.encode()
        ).digest()

        self.code_challenge = (
            base64.urlsafe_b64encode(digest)
            .decode()
            .replace("=", "")
        )

        self.state = secrets.token_urlsafe(32)

        return self

    # =====================================================
    # INFO
    # =====================================================

    def data(self):

        return {

            "code_verifier": self.code_verifier,

            "code_challenge": self.code_challenge,

            "code_challenge_method": "S256",

            "state": self.state,

        }

    # =====================================================
    # STATUS
    # =====================================================

    def ready(self):

        return bool(

            self.code_verifier
            and self.code_challenge
            and self.state

        )