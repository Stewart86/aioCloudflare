from api.commons.auth import Auth

from .schedules.schedules import Schedules


class Scripts(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "workers/scripts"
    _endpoint3 = None

    @property
    def schedules(self):
        return Schedules()
