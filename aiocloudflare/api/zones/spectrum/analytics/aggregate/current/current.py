from aiocloudflare.commons.auth import Auth


class Current(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics/aggregate/current"
    _endpoint3 = None
