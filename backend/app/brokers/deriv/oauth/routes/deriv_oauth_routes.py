from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
import traceback

from ..deriv_oauth_manager import DerivOAuthManager

router = APIRouter(
    prefix="/oauth/deriv",
    tags=["Deriv OAuth"],
)

oauth = DerivOAuthManager()


# =====================================================
# LOGIN
# =====================================================

@router.get("/login")
def login():

    print()
    print("=" * 80)
    print("🚀 LOGIN DERIV")
    print("=" * 80)

    try:

        url = oauth.login_url()

        print("URL:")
        print(url)

        print("=" * 80)

        return RedirectResponse(url=url)

    except Exception as e:

        print()
        print("❌ ERROR LOGIN")
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================================
# CALLBACK
# =====================================================

@router.get("/callback")
def callback(

    request: Request,

    code: str,

    state: str,

):

    print()
    print("=" * 80)
    print("🎉 CALLBACK DERIV")
    print("=" * 80)

    print("CODE:")
    print(code)

    print()
    print("STATE:")
    print(state)

    print()
    print("QUERY PARAMS:")
    print(dict(request.query_params))

    try:

        print()
        print("🔄 AUTORIZANDO...")

        token = oauth.authorize(code)

        print()
        print("✅ TOKEN RECIBIDO")
        print("-" * 60)

        print("ACCESS TOKEN:")
        print(token.access_token)

        print()

        print("TOKEN TYPE:")
        print(token.token_type)

        print()

        print("EXPIRES:")
        print(token.expires_in)

        print()

        print("REFRESH:")
        print(token.refresh_token)

        print()

        print("STATUS OAUTH")

        print(oauth.status())

        print("=" * 80)

        return {

            "ok": True,

            "access_token": token.access_token,

            "expires_in": token.expires_in,

            "token_type": token.token_type,

            "refresh_token": token.refresh_token,

            "oauth": oauth.status(),

        }

    except Exception as e:

        print()
        print("=" * 80)
        print("❌ ERROR CALLBACK")
        print("=" * 80)

        traceback.print_exc()

        print("=" * 80)

        raise HTTPException(

            status_code=500,

            detail=str(e),

        )


# =====================================================
# STATUS
# =====================================================

@router.get("/status")
def status():

    print()
    print("=" * 80)
    print("📊 OAUTH STATUS")
    print("=" * 80)

    data = oauth.status()

    print(data)

    print("=" * 80)

    return data


# =====================================================
# LOGOUT
# =====================================================

@router.get("/logout")
def logout():

    print()
    print("=" * 80)
    print("🚪 LOGOUT")
    print("=" * 80)

    oauth.logout()

    print("Sesión eliminada.")

    print("=" * 80)

    return {

        "ok": True,

    }