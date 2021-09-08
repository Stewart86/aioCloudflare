from aiocloudflare.commons.unused import Unused

from .filters.filters import Filters
from .routes.routes import Routes
from .script.script import Script


class Workers(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "workers"
    _endpoint3 = None

    @property
    def filters(self) -> Filters:
        return Filters(self._config, self._session)

    @property
    def routes(self) -> Routes:
        return Routes(self._config, self._session)

    @property
    def script(self) -> Script:
        return Script(self._config, self._session)
