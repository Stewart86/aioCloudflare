from api.commons.unused import Unused

from .scripts.scripts import Scripts


class Workers(Unused):
    _AUTH = "VOID"
    _endpoint1 = "user/workers"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def scripts(self):
        return Scripts()
