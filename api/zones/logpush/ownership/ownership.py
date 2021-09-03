from api.commons.auth import Auth

from .validate.validate import Validate


class Ownership(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "logpush/ownership"
    _endpoint3 = None

    @property
    def validate(self):
        return Validate()
