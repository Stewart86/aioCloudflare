from api.commons.auth import Auth


class AuditLogs(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/audit_logs"
    _endpoint2 = None
    _endpoint3 = None
