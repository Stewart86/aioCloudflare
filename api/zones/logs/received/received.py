from api.commons.auth_unwrapped import AuthUnwrapped

from .fields.fields import Fields


class Received(AuthUnwrapped):
    _AUTH = "AUTH_UNWRAPPED"
    _endpoint1 = "zones"
    _endpoint2 = "logs/received"
    _endpoint3 = None

    @property
    def fields(self):
        return Fields()
