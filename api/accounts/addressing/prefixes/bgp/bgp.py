from api.commons.unused import Unused

from .status.status import Status


class Bgp(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "addressing/prefixes"
    _endpoint3 = "bgp"

    @property
    def status(self):
        return Status()
