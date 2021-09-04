from dataclasses import dataclass
from logging import Logger
import os
from typing import Optional


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
    DEBUG: str = os.getenv("")
    TEST: bool = os.getenv("")
    LOGGER: Logger = None
    USER_AGENT: str = ""
