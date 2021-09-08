from aiocloudflare.commons.unused import Unused

from .control.control import Control
from .rayids.rayids import Rayids
from .received.received import Received


class Logs(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "logs"
    _endpoint3 = None

    @property
    def control(self) -> Control:
        return Control(self._config, self._session)

    @property
    def rayids(self) -> Rayids:
        return Rayids(self._config, self._session)

    @property
    def received(self) -> Received:
        return Received(self._config, self._session)
