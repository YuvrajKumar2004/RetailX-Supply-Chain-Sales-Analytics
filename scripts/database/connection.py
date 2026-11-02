"""
Database connection manager for RetailX.
"""

import os

from sqlalchemy import create_engine


DB_USER = os.getenv("DB_USER", "postgres")

DB_PASSWORD = os.getenv("DB_PASSWORD", "")

DB_HOST = os.getenv("DB_HOST", "localhost")

DB_PORT = os.getenv("DB_PORT", "5432")

DB_NAME = os.getenv("DB_NAME", "retailx_db")


DATABASE_URL = (

    f"postgresql+psycopg2://"

    f"{DB_USER}:{DB_PASSWORD}"

    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"

)

engine = create_engine(

    DATABASE_URL,

    future=True

)


def get_engine():

    return engine