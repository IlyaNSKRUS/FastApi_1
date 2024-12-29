import os


POSTGRES_DB = os.getenv("POSTGRES_DB", "netology_fastapi_db")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "qwerty12")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = (
    f"postgresql+asyncpg://"
    f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)