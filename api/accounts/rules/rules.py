from api.commons.unused import Unused

from .lists.lists import Lists


class Rules(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "rules"
    _endpoint3 = None

    @property
    def lists(self):
        return Lists()
