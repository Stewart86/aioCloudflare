from aiocloudflare.commons.auth import Auth


class ActivationCheck(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "activation_check"
    _endpoint3 = None
