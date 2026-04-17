import psycopg2
from config import get_db_settings


def open_connection():
    settings = get_db_settings()
    return psycopg2.connect(**settings)