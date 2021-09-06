import logging
from enum import Enum
from logging import Logger
from types import TracebackType
from typing import Optional, Type

from httpx import AsyncClient

from aiocloudflare.api.accounts.accounts import Accounts
from aiocloudflare.api.graphql.graphql import Graphql
from aiocloudflare.api.memberships.memberships import Memberships
from aiocloudflare.api.railguns.railguns import Railguns
from aiocloudflare.api.user.user import User
from aiocloudflare.api.zones.zones import Zones
from aiocloudflare.commons.config import Config

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
        raw: Optional[str] = None,  # TODO
        profile: Optional[str] = None,  # TODO
        user_agent: Optional[dict[str, str]] = None,
        base_url: Optional[str] = None,
        debug: Optional[bool] = False,
        test: Optional[bool] = None,  # TODO
        logger: Optional[Logger] = None,
        config: Optional[Config] = None,
    ) -> None:
        if config:
            self._config = config
        else:
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

        if b_url := self._config.BASE_URL:
            self._session = AsyncClient(base_url=b_url)

        self._state = ClientState.UNOPENED

    async def __aenter__(self) -> "Cloudflare":
        if self._state != ClientState.UNOPENED:
            msg = {
                ClientState.OPENED: "Cannot open a client instance more than once.",  # noqa
                ClientState.CLOSED: "Cannot reopen a client instance, once it has been closed.",  # noqa
            }[self._state]
            raise RuntimeError(msg)

        self._state = ClientState.OPENED
        await self._session.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        self._state = ClientState.CLOSED
        await self._session.__aexit__(exc_type, exc_value, traceback)

    async def aclose(self) -> None:
        await self._session.aclose()

    @property
    def accounts(self) -> Accounts:
        return Accounts(self._config, self._session)

    @property
    def graphql(self) -> Graphql:
        return Graphql(self._config, self._session)

    @property
    def memberships(self) -> Memberships:
        return Memberships(self._config, self._session)

    @property
    def railguns(self) -> Railguns:
        return Railguns(self._config, self._session)

    @property
    def user(self) -> User:
        return User(self._config, self._session)

    @property
    def zones(self) -> Zones:
        return Zones(self._config, self._session)
