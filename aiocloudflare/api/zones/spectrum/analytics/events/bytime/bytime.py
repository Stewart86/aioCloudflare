from aiocloudflare.commons.auth import Auth


class Bytime(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics/events/bytime"
    _endpoint3 = None
