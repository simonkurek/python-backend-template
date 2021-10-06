"""Config of DB"""
from pydantic import Field

from app.config.base import BaseSettings
from app.config.cfg import IS_TEST

import os
from dotenv import load_dotenv

load_dotenv()

DB_MODELS = ["app.core.models.db.City_Entity"]
POSTGRES_DB_URL = "postgres://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
SQLITE_DB_URL = "sqlite://:memory:"


class PostgresSettings:
    """Postgres env values"""

    def __init__(self):
        self.postgres_user = os.getenv("POSTGRES_USER")
        self.postgres_password = os.getenv("POSTGRES_PASSWORD")
        self.postgres_db = os.getenv("POSTGRES_DB")
        self.postgres_host = os.getenv("POSTGRES_HOST")
        self.postgres_port = os.getenv("POSTGRES_PORT")

    def get_db_url(self):
        return POSTGRES_DB_URL.format(
            postgres_user=self.postgres_user,
            postgres_password=self.postgres_password,
            postgres_host=self.postgres_host,
            postgres_port=self.postgres_port,
            postgres_db=self.postgres_db,
        )


postgres_settings = PostgresSettings()


class TortoiseSettings:

    def __init__(self):
        if IS_TEST:
            # sqlite
            self.db_url = SQLITE_DB_URL
            self.modules = {"models": DB_MODELS}
            self.generate_schemas = True
        else:
            # postgres
            self.db_url = postgres_settings.get_db_url()
            self.modules = {"models": DB_MODELS}
            self.generate_schemas = False
