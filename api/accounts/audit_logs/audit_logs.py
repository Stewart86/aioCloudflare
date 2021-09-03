from api.commons.auth import Auth


class AuditLogs(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "audit_logs"
    _endpoint3 = None
