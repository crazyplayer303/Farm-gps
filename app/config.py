"""Application configuration using environment variables."""

import os
from dotenv import load_dotenv

# Load variables from .env file if present
load_dotenv()

class Config:
    """Base configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///farms.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    """Configuration used during tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

# Map environment name to config
config_by_name = {
    "testing": TestingConfig,
    "default": Config,
}
