from api.commons.auth import Auth

from .fallback_origin.fallback_origin import FallbackOrigin


class CustomHostnames(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "custom_hostnames"
    _endpoint3 = None

    @property
    def fallback_origin(self):
        return FallbackOrigin()
