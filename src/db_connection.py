import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        host = os.getenv("PG_HOST", "localhost"),
        database = os.getenv("PG_DB", "reconciliation_db"),
        user = os.getenv("PG_USER", "postgres"),
        password = os.getenv("PG_PASSWORD", "Sairam9#"),
        port = os.getenv("PG_PORT", "5432")

    )