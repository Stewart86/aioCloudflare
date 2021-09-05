from aiocloudflare.commons.auth import Auth


class SortQueryStringForCache(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/sort_query_string_for_cache"
    _endpoint3 = None
