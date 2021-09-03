from logging import Logger
import logging
from api.commons.config import Config
from typing import Optional
from api.accounts.accounts import Accounts
from api.graphql.graphql import Graphql
from api.memberships.memberships import Memberships
from api.railguns.railguns import Railguns
from api.user.user import User
from api.zones.zones import Zones


LOGGER = logging.getLogger(__name__)


class Cloudflare:
    def __init__(
        self,
        email: Optional[str] = None,
        token: Optional[str] = None,
        certtoken: Optional[str] = None,
        raw: Optional[str] = False,
        profile: Optional[str] = None,
        user_agent: Optional[dict[str, str]] = None,
        base_url: Optional[str] = None,
        debug: Optional[bool] = False,
        test: Optional[bool] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        self._config = Config(
            EMAIL=email,
            TOKEN=token,
            CERTTOKEN=certtoken,
            RAW=raw,
            PROFILE=profile,
            BASE_URL=base_url,
            USER_AGENT=user_agent,
            DEBUG=debug,
            TEST=test if test is not None else True,
            LOGGER=logger if logger is not None else LOGGER,
        )

    @property
    def accounts(self):
        return Accounts()

    @property
    def graphql(self):
        return Graphql()

    @property
    def memberships(self):
        return Memberships()

    @property
    def railguns(self):
        return Railguns()

    @property
    def user(self):
        return User()

    @property
    def zones(self):
        return Zones()
