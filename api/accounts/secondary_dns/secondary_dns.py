from api.commons.unused import Unused

from .masters.masters import Masters
from .primaries.primaries import Primaries
from .tsigs.tsigs import Tsigs


class SecondaryDns(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "secondary_dns"
    _endpoint3 = None

    @property
    def masters(self):
        return Masters()

    @property
    def primaries(self):
        return Primaries()

    @property
    def tsigs(self):
        return Tsigs()
