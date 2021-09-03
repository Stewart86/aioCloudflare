from api.commons.auth import Auth

from .preview.preview import Preview


class Healthchecks(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "healthchecks"
    _endpoint3 = None

    @property
    def preview(self):
        return Preview()
