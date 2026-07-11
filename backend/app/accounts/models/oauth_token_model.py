from dataclasses import dataclass


@dataclass
class OAuthTokenModel:

    access_token: str

    refresh_token: str | None = None

    token_type: str = "Bearer"

    expires_in: int = 0