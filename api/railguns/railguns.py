from api.commons.auth import Auth

from .zones.zones import Zones


class Railguns(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "railguns"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def zones(self):
        return Zones()
