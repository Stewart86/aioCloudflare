from aiocloudflare.commons.unused import Unused

from .prefixes.prefixes import Prefixes


class Addressing(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "addressing"
    _endpoint3 = None

    @property
    def prefixes(self) -> Prefixes:
        return Prefixes(self._config, self._session)
