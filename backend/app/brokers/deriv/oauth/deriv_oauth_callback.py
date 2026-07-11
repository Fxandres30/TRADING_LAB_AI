from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# =====================================================
# TOKEN
# =====================================================

@dataclass(slots=True)
class DerivOAuthToken:

    access_token: str

    token_type: str = "Bearer"

    expires_in: int = 0

    refresh_token: Optional[str] = None

    created_at: datetime = field(default_factory=datetime.utcnow)


# =====================================================
# ACCOUNT
# =====================================================

@dataclass(slots=True)
class DerivOAuthAccount:

    loginid: str

    email: str

    currency: str

    is_virtual: bool

    balance: float = 0


# =====================================================
# PROFILE
# =====================================================

@dataclass(slots=True)
class DerivOAuthProfile:

    user_id: str

    fullname: str

    email: str


# =====================================================
# SESSION
# =====================================================

@dataclass(slots=True)
class DerivOAuthSession:

    broker: str = "deriv"

    connected: bool = False

    account: Optional[DerivOAuthAccount] = None

    token: Optional[DerivOAuthToken] = None

    profile: Optional[DerivOAuthProfile] = None