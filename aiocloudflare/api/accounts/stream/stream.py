from aiocloudflare.commons.auth import Auth

from .captions.captions import Captions
from .copy.copy import Copy
from .direct_upload.direct_upload import DirectUpload
from .embed.embed import Embed
from .keys.keys import Keys
from .preview.preview import Preview
from .watermarks.watermarks import Watermarks
from .webhook.webhook import Webhook


class Stream(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "stream"
    _endpoint3 = None

    @property
    def watermarks(self) -> Watermarks:
        return Watermarks(self._config, self._session)

    @property
    def captions(self) -> Captions:
        return Captions(self._config, self._session)

    @property
    def embed(self) -> Embed:
        return Embed(self._config, self._session)

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)

    @property
    def direct_upload(self) -> DirectUpload:
        return DirectUpload(self._config, self._session)

    @property
    def webhook(self) -> Webhook:
        return Webhook(self._config, self._session)

    @property
    def copy(self) -> Copy:
        return Copy(self._config, self._session)

    @property
    def keys(self) -> Keys:
        return Keys(self._config, self._session)
