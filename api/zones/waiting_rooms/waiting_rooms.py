from api.commons.auth import Auth

from .status.status import Status
from .preview.preview import Preview


class WaitingRooms(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "waiting_rooms"
    _endpoint3 = None

    @property
    def status(self):
        return Status()

    @property
    def preview(self):
        return Preview()
