from enum import Enum
from logging import Logger
import logging
from types import TracebackType
from httpx import AsyncClient

from api.commons.config import Config
from typing import Optional, Type
from api.accounts.accounts import Accounts
from api.graphql.graphql import Graphql
from api.memberships.memberships import Memberships
from api.railguns.railguns import Railguns
from api.user.user import User
from api.zones.zones import Zones


LOGGER = logging.getLogger(__name__)


class ClientState(Enum):
    # UNOPENED:
    #   The client has been instantiated, but has not been used to send a request,
    #   or been opened by entering the context of a `with` block.
    UNOPENED = 1
    # OPENED:
    #   The client has either sent a request, or is within a `with` block.
    OPENED = 2
    # CLOSED:
    #   The client has either exited the `with` block, or `close()` has
    #   been called explicitly.
    CLOSED = 3


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

        self._state = ClientState.UNOPENED
        self._session = AsyncClient()

    async def __aenter__(self):
        if self._state != ClientState.UNOPENED:
            msg = {
                ClientState.OPENED: "Cannot open a client instance more than once.",
                ClientState.CLOSED: "Cannot reopen a client instance, once it has been closed.",
            }[self._state]
            raise RuntimeError(msg)

        self._state = ClientState.OPENED
        await self._session.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        self._state = ClientState.CLOSED
        await self._session.__aexit__(exc_type, exc_value, traceback)

    async def aclose(self):
        await self._session.aclose()

    @property
    def accounts(self):
        return Accounts(self._config, self._session)

    @property
    def graphql(self):
        return Graphql(self._config, self._session)

    @property
    def memberships(self):
        return Memberships(self._config, self._session)

    @property
    def railguns(self):
        return Railguns(self._config, self._session)

    @property
    def user(self):
        return User(self._config, self._session)

    @property
    def zones(self):
        return Zones(self._config, self._session)
