import os

from dotenv import dotenv_values
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # =====================================================
    # APP
    # =====================================================

    APP_NAME: str = "Trading Lab AI"
    VERSION: str = "2.0.0"
    DESCRIPTION: str = "Framework Profesional de Trading Algorítmico"

    # =====================================================
    # API
    # =====================================================

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    DEBUG: bool = True

    # =====================================================
    # BROKER
    # =====================================================

    DEFAULT_BROKER: str = "deriv"

    # =====================================================
# DERIV
# =====================================================

    DERIV_APP_ID: str = ""

    DERIV_CLIENT_ID: str = ""

    DERIV_REDIRECT_URI: str = ""

    # =====================================================
    # MT5
    # =====================================================

    MT5_LOGIN: int | None = None
    MT5_PASSWORD: str = ""
    MT5_SERVER: str = ""

    # =====================================================
    # SUPABASE
    # =====================================================

    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    # =====================================================
    # DATABASE
    # =====================================================

    DATABASE_URL: str = ""

    # =====================================================
    # LOGS
    # =====================================================

    LOG_LEVEL: str = "INFO"

    # =====================================================
    # CONFIG
    # =====================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


# ==========================================================
# DEPURACIÓN
# ==========================================================

print("\n" + "=" * 60)
print("CONFIGURACIÓN ENCONTRADA")
print("=" * 60)

print("\n📄 .env")

for k, v in dotenv_values(".env").items():
    print(f"{k} = {v}")

# ==========================
# CREAR SETTINGS
# ==========================

settings = Settings()

print("\n⚙️ CONFIGURACIÓN CARGADA")

print("DERIV_APP_ID        =", settings.DERIV_APP_ID)
print("DERIV_CLIENT_ID     =", settings.DERIV_CLIENT_ID)
print("DERIV_REDIRECT_URI  =", settings.DERIV_REDIRECT_URI)

print("=" * 60)


settings = Settings()