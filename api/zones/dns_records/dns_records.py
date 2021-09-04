from api.commons.auth import Auth


class DnsRecords(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "dns_records"
    _endpoint3 = None
