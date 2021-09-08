import os
from dataclasses import dataclass
from logging import Logger
from typing import Any, Optional

try:
    import dotenv

    dotenv.load_dotenv(".env")
except ImportError:
    pass


ENV = os.getenv("CF_API_EMAIL")


@dataclass(init=True)
class Config:
    EMAIL: Optional[str]
    TOKEN: Optional[str]
    CERTTOKEN: Optional[str]
    RAW: Optional[str]
    PROFILE: Optional[str]
    BASE_URL: Optional[str]
    DEBUG: bool
    TEST: bool
    LOGGER: Logger
    USER_AGENT: str

    def __init__(
        self,
        email: Optional[str] = None,
        token: Optional[str] = None,
        certtoken: Optional[str] = None,
        user_agent: Optional[dict[str, str]] = None,
        base_url: Optional[str] = None,
        debug: Optional[bool] = False,
    ) -> None:
        self.EMAIL = self.__env_or_init(email, "CF_API_EMAIL")
        self.TOKEN = self.__env_or_init(token, "CF_API_KEY")
        self.CERTTOKEN = self.__env_or_init(certtoken, "CF_API_CERTKEY")
        self.USER_AGENT: str = self.__env_or_init(
            user_agent, "USER_AGENT", "aiocloudflare"
        )
        self.BASE_URL = self.__env_or_init(
            base_url, "CF_API_URL", "https://api.cloudflare.com/client/v4"
        )
        self.DEBUG = self.__env_or_init(debug, "DEBUG", False)

    def __env_or_init(
        self, var: Any, env_key: str, default_value: Optional[Any] = None
    ) -> Any:
        if var is None:
            if default_value:
                return os.getenv(env_key, default_value)
            return os.getenv(env_key)
        return var
