import json
from pathlib import Path
from typing import Dict

from pydantic import Field, FilePath
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings model from environment"""

    database_host: str = Field("localhost", env="DATABASE_HOST")
    database_user: str = Field("test", env="DATABASE_USER")
    database_password: str = Field("test", env="DATABASE_PASSWORD")
    database_name: str = Field("postgres", env="DATABASE_NAME")
    CORS_ALLOW_ORIGINS: str = Field("*", env="CORS_ALLOW_ORIGINS")

    @property
    def db_uri(self) -> str:
        """Database URI"""
        return (
            f"postgresql://{self.database_user}:{self.database_password}@"
            f"{self.database_host}:5432/{self.database_name}"
        )


settings = Settings()


class LogEnvSettings(BaseSettings):
    """Settings model from log configuration"""

    LOG_CONFIG: FilePath = Path(__file__).parent / "log_config/base_log_config.json"


def load_log_configuration() -> Dict:
    """Load log configuration from file"""
    with LogEnvSettings().LOG_CONFIG.open(encoding="UTF-8") as conf_file:
        logconfig_dict: Dict = json.load(conf_file)

    return logconfig_dict
