import os

from config import (
    DB_USER, DB_NAME, DB_PASS, DB_HOST, DB_PORT, BASE_URL_KINOPOISK, API_KEY_KINOPOISK)

SECRET_KEY = b"SECRET_KEY"
# Secret key
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

# Data Base
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# KinopoiskApi
BASE_URL_KINOPOISK = BASE_URL_KINOPOISK
API_KEY_KINOPOISK = API_KEY_KINOPOISK
