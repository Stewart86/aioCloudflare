from api.commons.unused import Unused

from .analyze.analyze import Analyze
from .certificate_packs.certificate_packs import CertificatePacks
from .verification.verification import Verification
from .universal.universal import Universal


class Ssl(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "ssl"
    _endpoint3 = None

    @property
    def analyze(self):
        return Analyze()

    @property
    def certificate_packs(self):
        return CertificatePacks()

    @property
    def verification(self):
        return Verification()

    @property
    def universal(self):
        return Universal()
