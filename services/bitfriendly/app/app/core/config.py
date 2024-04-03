from typing import Any, Dict, List, Optional, Union
import os
from pydantic.networks import AnyHttpUrl, EmailStr, HttpUrl
from pydantic_settings import BaseSettings
from pydantic import validator
import secrets
from dotenv import load_dotenv



class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # print( SECRET_KEY)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = 'https://184.94.215.245:2087'
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1:8080"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [  "http://localhost",
    #                                             "http://localhost:8080",
    #                                             "https://bitfriendly.me",
    #                                              "http://127.0.0.1:8000",
    #                                               "http://127.0.0.1"
    #                                              ]


    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = 'BITFRIENDLY'
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if v is None or len(v) == 0:
            return None
        return v

    class Config:
        case_sensitive = True

settings = Settings()
