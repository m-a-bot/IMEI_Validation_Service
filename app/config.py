from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # General settings
    APP_TITLE: str
    APP_VERSION: str
    LOG_LEVEL: str

    # FastAPI Settings
    FASTAPI_HOST: str
    FASTAPI_PORT: int

    # ACCESS CONTROL SERVICE
    VERIFY_TOKEN_URL: str

    # imeicheck.net validation service
    IMEI_API_NAME: str = "imeicheck.net"

    IMEICHECK_VALIDATION_URL: str
    USE_SANDBOX: bool = True
    IMEICHECK_TOKEN_SANDBOX: str
    IMEICHECK_TOKEN_LIVE: str
    IMEI_CHECKS_URL: str = "/v1/checks"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
