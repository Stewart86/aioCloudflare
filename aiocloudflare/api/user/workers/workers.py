from aiocloudflare.commons.unused import Unused

from .scripts.scripts import Scripts


class Workers(Unused):
    _endpoint1 = "user/workers"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def scripts(self) -> Scripts:
        return Scripts(self._config, self._session)
