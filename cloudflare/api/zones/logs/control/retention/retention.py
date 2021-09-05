from cloudflare.commons.unused import Unused

from .flag.flag import Flag


class Retention(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "logs/control/retention"
    _endpoint3 = None

    @property
    def flag(self):
        return Flag(self._config, self._session)
