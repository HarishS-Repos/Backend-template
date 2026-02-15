from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "local"
    LLM_TIMEOUT: int = 30
    JWT_ISSUER: str
    JWT_AUDIENCE: str

    class Config:
        env_file = ".env"

settings = Settings()
