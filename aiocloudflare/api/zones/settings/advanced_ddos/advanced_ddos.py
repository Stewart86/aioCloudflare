from aiocloudflare.commons.auth import Auth


class AdvancedDdos(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/advanced_ddos"
    _endpoint3 = None
