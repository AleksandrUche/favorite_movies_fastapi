import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

API_KEY_KINOPOISK = os.environ.get('API_KEY_KINOPOISK')
BASE_URL_KINOPOISK = os.environ.get('BASE_URL_KINOPOISK')
