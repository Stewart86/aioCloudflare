import os
from dataclasses import dataclass
from logging import Logger
from typing import Optional

try:
    import dotenv
except ImportError:
    dotenv = None

if dotenv:
    dotenv.load_dotenv()


@dataclass(init=True, frozen=True)
class Config:
    EMAIL: Optional[str] = os.getenv("CF_API_EMAIL")
    TOKEN: Optional[str] = os.getenv("CF_API_KEY")
    CERTTOKEN: Optional[str] = os.getenv("CF_API_CERTKEY")
    RAW: Optional[str] = False
    PROFILE: Optional[str] = os.getenv("")
    BASE_URL: Optional[str] = os.getenv(
        "CF_API_URL", "https://api.cloudflare.com/client/v4"
    )
    DEBUG: bool = os.getenv("", False)
    TEST: bool = os.getenv("", False)
    LOGGER: Logger = None
    USER_AGENT: str = "aiocloudflare".encode("ascii")
