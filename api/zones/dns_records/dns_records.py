from api.commons.auth import Auth

from .export.export import Export
from .import_.import_ import Import_


class DnsRecords(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "dns_records"
    _endpoint3 = None

    @property
    def export(self):
        return Export()

    @property
    def import_(self):
        return Import_()
