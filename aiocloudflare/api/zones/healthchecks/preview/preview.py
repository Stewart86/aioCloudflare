from aiocloudflare.commons.auth import Auth


class Preview(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "healthchecks/preview"
    _endpoint3 = None
