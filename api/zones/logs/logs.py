from api.commons.unused import Unused

from .control.control import Control
from .received.received import Received
from .rayids.rayids import Rayids


class Logs(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "logs"
    _endpoint3 = None

    @property
    def control(self):
        return Control()

    @property
    def received(self):
        return Received()

    @property
    def rayids(self):
        return Rayids()
