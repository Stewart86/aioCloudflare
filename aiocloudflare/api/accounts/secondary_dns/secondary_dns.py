from aiocloudflare.commons.unused import Unused

from .masters.masters import Masters
from .primaries.primaries import Primaries
from .tsigs.tsigs import Tsigs


class SecondaryDns(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "secondary_dns"
    _endpoint3 = None

    @property
    def tsigs(self) -> Tsigs:
        return Tsigs(self._config, self._session)

    @property
    def masters(self) -> Masters:
        return Masters(self._config, self._session)

    @property
    def primaries(self) -> Primaries:
        return Primaries(self._config, self._session)
