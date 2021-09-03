from api.commons.unused import Unused

from .fields.fields import Fields
from .jobs.jobs import Jobs


class Datasets(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "logpush/datasets"
    _endpoint3 = None

    @property
    def fields(self):
        return Fields()

    @property
    def jobs(self):
        return Jobs()
