from urllib.parse import urlencode

import requests

from app.config.settings import settings

from .deriv_oauth_pkce import DerivOAuthPKCE
from .deriv_oauth_storage import storage


class DerivOAuthClient:

    AUTH_URL = "https://auth.deriv.com/oauth2/auth"
    TOKEN_URL = "https://auth.deriv.com/oauth2/token"

    def __init__(self):

        self.client_id = settings.DERIV_CLIENT_ID
        self.redirect_uri = settings.DERIV_REDIRECT_URI
        self.scope = "trade account_manage"

    # =====================================================
    # LOGIN URL
    # =====================================================

    def authorization_url(self):

        pkce = DerivOAuthPKCE().generate()

        data = pkce.data()

        storage.save(

            state=data["state"],

            code_verifier=data["code_verifier"],

            code_challenge=data["code_challenge"],

        )

        print()
        print("=" * 80)
        print("🚀 DERIV OAUTH")
        print("=" * 80)

        print("AUTH URL      :", self.AUTH_URL)
        print("TOKEN URL     :", self.TOKEN_URL)

        print("APP ID        :", settings.DERIV_APP_ID)
        print("CLIENT ID     :", self.client_id)
        print("REDIRECT URI  :", self.redirect_uri)
        print("SCOPE         :", self.scope)

        print("STATE         :", data["state"])
        print("VERIFIER      :", data["code_verifier"])
        print("CHALLENGE     :", data["code_challenge"])

        params = {

            "response_type": "code",

            "client_id": self.client_id,

            "redirect_uri": self.redirect_uri,

            "scope": self.scope,

            "state": data["state"],

            "code_challenge": data["code_challenge"],

            "code_challenge_method": "S256",

        }

        print()
        print("PARAMETROS")
        print("-" * 80)

        for k, v in params.items():
            print(f"{k:25}: {v}")

        url = f"{self.AUTH_URL}?{urlencode(params)}"

        print()
        print("URL FINAL")
        print("-" * 80)
        print(url)

        print()
        print("STORAGE")
        print(storage.status())

        print("=" * 80)

        return url

    # =====================================================
    # TOKEN
    # =====================================================

    def exchange_code(

        self,

        code: str,

        state: str,

    ):

        session = storage.get(state)

        if session is None:

            raise Exception(
                f"No existe una sesión PKCE para el state: {state}"
            )

        payload = {

            "grant_type": "authorization_code",

            "client_id": self.client_id,

            "code": code,

            "redirect_uri": self.redirect_uri,

            "code_verifier": session["code_verifier"],

        }

        print()
        print("=" * 80)
        print("🔄 INTERCAMBIO TOKEN")
        print("=" * 80)

        print("STATE:", state)

        print()
        print("PAYLOAD")
        print("-" * 80)

        for k, v in payload.items():
            print(f"{k:20}: {v}")

        response = requests.post(

            self.TOKEN_URL,

            data=payload,

            timeout=30,

        )

        print()
        print("RESPUESTA")
        print("-" * 80)

        print("STATUS:", response.status_code)

        try:
            print(response.json())
        except Exception:
            print(response.text)

        print("=" * 80)

        response.raise_for_status()

        storage.remove(state)

        return response.json()