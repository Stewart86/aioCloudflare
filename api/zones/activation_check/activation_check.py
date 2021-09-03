from api.commons.auth import Auth


class ActivationCheck(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "activation_check"
    _endpoint3 = None
