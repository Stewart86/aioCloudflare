from api.commons.unused import Unused

from .scripts.scripts import Scripts


class Workers(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "workers"
    _endpoint3 = None

    @property
    def scripts(self):
        return Scripts()
