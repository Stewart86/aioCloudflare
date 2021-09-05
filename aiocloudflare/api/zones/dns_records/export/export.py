from aiocloudflare.commons.auth import Auth


class Export(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "dns_records/export"
    _endpoint3 = None
