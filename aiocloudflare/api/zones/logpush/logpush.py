from aiocloudflare.commons.unused import Unused

from .datasets.datasets import Datasets
from .jobs.jobs import Jobs
from .ownership.ownership import Ownership
from .validate.validate import Validate


class Logpush(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "logpush"
    _endpoint3 = None

    @property
    def validate(self) -> Validate:
        return Validate(self._config, self._session)

    @property
    def jobs(self) -> Jobs:
        return Jobs(self._config, self._session)

    @property
    def datasets(self) -> Datasets:
        return Datasets(self._config, self._session)

    @property
    def ownership(self) -> Ownership:
        return Ownership(self._config, self._session)
