from aiocloudflare.commons.unused import Unused

from .events.events import Events


class Security(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "security"
    _endpoint3 = None

    @property
    def events(self) -> Events:
        return Events(self._config, self._session)
