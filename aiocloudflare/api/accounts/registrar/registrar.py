from aiocloudflare.commons.unused import Unused

from .domains.domains import Domains


class Registrar(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "registrar"
    _endpoint3 = None

    @property
    def domains(self) -> Domains:
        return Domains(self._config, self._session)
