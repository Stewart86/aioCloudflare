from aiocloudflare.commons.auth import Auth


class Certificates(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "origin_tls_client_auth/hostnames/certificates"
    _endpoint3 = None
