from api.accounts.accounts import Accounts
from api.graphql.graphql import Graphql
from api.memberships.memberships import Memberships
from api.railguns.railguns import Railguns
from api.user.user import User
from api.zones.zones import Zones


class Cloudflare:
    @property
    def accounts(self):
        return Accounts()

    @property
    def graphql(self):
        return Graphql()

    @property
    def memberships(self):
        return Memberships()

    @property
    def railguns(self):
        return Railguns()

    @property
    def user(self):
        return User()

    @property
    def zones(self):
        return Zones()
