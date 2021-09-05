from aiocloudflare.commons.auth import Auth


class DnsRecords(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "dns_records"
    _endpoint3 = None
