from api.commons.auth import Auth


class CustomHostnames(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "custom_hostnames"
    _endpoint3 = None
