import os
from functools import lru_cache
from dotenv import load_dotenv

@lru_cache()
def get_settings():
    load_dotenv( f".env.{os.getenv('APP_MOD')}" )
    return Settings()

class Settings:
    app_name: str = "FastAPI with Uvicorn"
    app_version: str = "0.1.0"

    app_mode: str = os.getenv("APP_MOD")
    port: int = int(os.getenv("PORT"))
    reload: bool = bool(os.getenv("RELOAD"))
    http_proxy: str = os.getenv("HTTP_PROXY")
    https_proxy: str = os.getenv("HTTPS_PROXY")
    database_url: str = os.getenv("DATABASE_URL")