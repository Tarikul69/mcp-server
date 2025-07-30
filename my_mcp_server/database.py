import sqlite3
import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "sqlite")

def get_db_connection():
    if DB_TYPE == "sqlite":
        conn = sqlite3.connect(os.getenv("DB_NAME", "leave.db"))
    elif DB_TYPE == "postgres":
        conn = psycopg.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
    else:
        raise Exception("Unsupported DB type")
    return conn
