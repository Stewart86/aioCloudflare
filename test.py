from cloudflare import Cloudflare
import asyncio


async def async_main():
    async with Cloudflare() as cf:
        await cf.zones.get()
        await cf.zones.get()
        await cf.zones.get()
        await cf.zones.get()
        await cf.zones.get()
        await cf.zones.get()
        await cf.zones.get()


def main():
    # cf = Cloudflare()
    # cf.user.invites.get()
    # cf.user.billing.history.get()
    # cf.zones.settings.ssl.get("1")
    # cf.zones.dns_records.get("1")
    # cf.zones.logs.received.get("df")

    # cf.zones.origin_tls_client_auth.hostnames.certificates.get("sdf")

    # # import is written as import_ as import is a python keyword
    # cf.zones.dns_records.import_.get("1")
    # cf.accounts.rulesets.import_.patch("1")

    # # 0rtt is written as ortt as class name does not allow digit as a start of the name
    # cf.zones.settings.ortt.get("1")
    pass


if "__main__" == __name__:
    asyncio.run(async_main())
