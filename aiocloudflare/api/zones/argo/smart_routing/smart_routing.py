from aiocloudflare.commons.auth import Auth


class SmartRouting(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "argo/smart_routing"
    _endpoint3 = None
