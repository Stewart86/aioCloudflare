from aiocloudflare.commons.auth import Auth


class Flag(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "logs/control/retention/flag"
    _endpoint3 = None
