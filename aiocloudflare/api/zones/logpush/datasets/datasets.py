from aiocloudflare.commons.unused import Unused

from .fields.fields import Fields
from .jobs.jobs import Jobs


class Datasets(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "logpush/datasets"
    _endpoint3 = None

    @property
    def fields(self) -> Fields:
        return Fields(self._config, self._session)

    @property
    def jobs(self) -> Jobs:
        return Jobs(self._config, self._session)
