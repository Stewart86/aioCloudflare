from api.commons.unused import Unused

from .domains.domains import Domains


class Registrar(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "registrar"
    _endpoint3 = None

    @property
    def domains(self):
        return Domains()
