from api.commons.unused import Unused

from .datasets.datasets import Datasets
from .jobs.jobs import Jobs
from .ownership.ownership import Ownership
from .validate.validate import Validate


class Logpush(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "logpush"
    _endpoint3 = None

    @property
    def datasets(self):
        return Datasets()

    @property
    def jobs(self):
        return Jobs()

    @property
    def ownership(self):
        return Ownership()

    @property
    def validate(self):
        return Validate()
