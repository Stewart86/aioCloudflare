from api.commons.no_auth import NoAuth

from httpx._models import Response
from httpx._types import (
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
)

from api.commons.exceptions import CloudflareMethodNotAvailable


class Unused(NoAuth):
    def __repr__(self) -> str:
        return f"derived from: Unused, class: {self.__class__.__name__}"

    async def get(
        self,
        *args: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
    ) -> Response:
        """Method is not available
        ---
        """
        raise CloudflareMethodNotAvailable("Method is not available for the endpoint.")
