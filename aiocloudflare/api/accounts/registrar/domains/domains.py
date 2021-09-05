from aiocloudflare.commons.auth import Auth


class Domains(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "registrar/domains"
    _endpoint3 = None
