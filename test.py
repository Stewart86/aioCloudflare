import asyncio
import logging

from aiocloudflare.cloudflare import Cloudflare

logging.basicConfig(level=logging.DEBUG)


async def async_main() -> None:
    tasks = [asyncio.create_task(get_zone()) for _ in range(1)]
    await asyncio.gather(*tasks)


async def get_zone() -> None:
    async with Cloudflare(debug=True) as cf:
        await cf.zones.post()
        await cf.zones.settings.get("ss")


def main() -> None:
    # cf = Cloudflare()
    # cf.user.invites.get()
    # cf.user.billing.history.get()
    # cf.zones.settings.ssl.get("1")
    # cf.zones.dns_records.get("1")
    # cf.zones.logs.received.get("df")

    # await cf.zones.analytics.get()
    # cf.zones.origin_tls_client_auth.hostnames.certificates.get("sdf")

    # # import is written as import_ as import is a python keyword
    # cf.zones.dns_records.import_.get("1")
    # cf.accounts.rulesets.import_.patch("1")

    # # 0rtt is written as ortt as class name does not allow digit
    # as a start of the name
    # cf.zones.settings.ortt.get("1")
    pass


if "__main__" == __name__:
    asyncio.run(async_main())
