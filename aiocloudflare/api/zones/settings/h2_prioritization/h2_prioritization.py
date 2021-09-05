from aiocloudflare.commons.auth import Auth


class H2Prioritization(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/h2_prioritization"
    _endpoint3 = None
