from aiocloudflare.commons.unused import Unused

from .analyze.analyze import Analyze
from .certificate_packs.certificate_packs import CertificatePacks
from .universal.universal import Universal
from .verification.verification import Verification


class Ssl(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "ssl"
    _endpoint3 = None

    @property
    def certificate_packs(self) -> CertificatePacks:
        return CertificatePacks(self._config, self._session)

    @property
    def verification(self) -> Verification:
        return Verification(self._config, self._session)

    @property
    def universal(self) -> Universal:
        return Universal(self._config, self._session)

    @property
    def analyze(self) -> Analyze:
        return Analyze(self._config, self._session)
