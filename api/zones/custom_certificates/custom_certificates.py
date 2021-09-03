from api.commons.auth import Auth

from .prioritize.prioritize import Prioritize


class CustomCertificates(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "custom_certificates"
    _endpoint3 = None

    @property
    def prioritize(self):
        return Prioritize()
