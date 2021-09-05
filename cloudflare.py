import logging
from enum import Enum
from logging import Logger
from types import TracebackType
from typing import Optional, Type

from httpx import AsyncClient
from httpx._client import BaseClient

from api.accounts.accounts import Accounts
from api.commons.config import Config
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
        raw: Optional[str] = False,  # TODO
        profile: Optional[str] = None,  # TODO
        user_agent: Optional[dict[str, str]] = None,
        base_url: Optional[str] = None,
        debug: Optional[bool] = False,
        test: Optional[bool] = None,  # TODO
        logger: Optional[Logger] = None,
        session: Optional[BaseClient] = None,
    ) -> None:
        self._config = Config(
            email,
            token,
            certtoken,
            raw,
            profile,
            user_agent,
            base_url,
            debug,
            test,
        )

        if logger:
            self._config.LOGGER = logger
        else:
            self._config.LOGGER = LOGGER

        # session default to AsyncClient
        if session is None:
            self._session = AsyncClient(base_url=self._config.BASE_URL)
        else:
            self._session = session

        self._state = ClientState.UNOPENED

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
