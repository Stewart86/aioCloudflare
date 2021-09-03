from api.commons.auth import Auth

from .diagnose.diagnose import Diagnose


class Railguns(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "railguns"
    _endpoint3 = None

    @property
    def diagnose(self):
        return Diagnose()
