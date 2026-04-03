import psycopg2
from config import get_db_settings


def open_connection():
    settings = get_db_settings()
    connection = psycopg2.connect(**settings)
    return connection