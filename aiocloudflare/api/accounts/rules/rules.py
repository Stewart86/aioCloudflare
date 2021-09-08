from aiocloudflare.commons.unused import Unused

from .lists.lists import Lists


class Rules(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "rules"
    _endpoint3 = None

    @property
    def lists(self) -> Lists:
        return Lists(self._config, self._session)
