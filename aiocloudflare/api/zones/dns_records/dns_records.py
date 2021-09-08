from aiocloudflare.commons.auth import Auth

from .export.export import Export
from .import_.import_ import Import_


class DnsRecords(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "dns_records"
    _endpoint3 = None

    @property
    def export(self) -> Export:
        return Export(self._config, self._session)

    @property
    def import_(self) -> Import_:
        return Import_(self._config, self._session)
