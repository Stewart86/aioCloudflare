from api.commons.auth import Auth

from .retention.retention import Retention


class Control(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "logs/control"
    _endpoint3 = None

    @property
    def retention(self):
        return Retention()
