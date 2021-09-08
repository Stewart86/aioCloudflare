from aiocloudflare.commons.auth import Auth

from .preview.preview import Preview
from .status.status import Status


class WaitingRooms(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "waiting_rooms"
    _endpoint3 = None

    @property
    def status(self) -> Status:
        return Status(self._config, self._session)

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)
