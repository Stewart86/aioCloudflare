from api.commons.unused import Unused

from .prefixes.prefixes import Prefixes


class Addressing(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "addressing"
    _endpoint3 = None

    @property
    def prefixes(self):
        return Prefixes()
