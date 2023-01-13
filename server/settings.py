from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str
    server_host: str
    server_port: int
    database_url: str
    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expires_s: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='UTF-8'
)