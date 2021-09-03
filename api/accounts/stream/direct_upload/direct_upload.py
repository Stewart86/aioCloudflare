from api.commons.auth import Auth


class DirectUpload(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "stream/direct_upload"
    _endpoint3 = None
