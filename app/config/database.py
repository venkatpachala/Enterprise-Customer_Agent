from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DB_",
        extra="ignore",
    )

    host: str = Field(default="localhost")
    port: int = Field(default=5432)
    user: str = Field(default="postgres")
    password: str = Field(default="postgres")
    database: str = Field(default="aegis")

@property
def url(self) -> str:
    return (
        f"postgresql+psycopg://"
        f"{self.user}:{self.password}"
        f"@{self.host}:{self.port}"
        f"/{self.database}"
    )