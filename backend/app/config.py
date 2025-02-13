"""
Configuration for the application based on the environment.
"""

import os
from .config_local import SQLALCHEMY_DATABASE_URL as LOCAL_DB_URL

ENV = os.getenv("ENV", "production")

if ENV == "production":
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
else:
    SQLALCHEMY_DATABASE_URL = LOCAL_DB_URL