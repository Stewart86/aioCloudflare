from api.commons.unused import Unused

from .filters.filters import Filters
from .routes.routes import Routes
from .script.script import Script


class Workers(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "workers"
    _endpoint3 = None

    @property
    def filters(self):
        return Filters()

    @property
    def routes(self):
        return Routes()

    @property
    def script(self):
        return Script()
