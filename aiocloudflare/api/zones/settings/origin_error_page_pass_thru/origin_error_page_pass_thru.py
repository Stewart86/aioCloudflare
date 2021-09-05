from aiocloudflare.commons.auth import Auth


class OriginErrorPagePassThru(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/origin_error_page_pass_thru"
    _endpoint3 = None
