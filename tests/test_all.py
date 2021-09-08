import httpx
import pytest

from aiocloudflare.cloudflare import Cloudflare


@pytest.mark.asyncio
async def test_user(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_billing(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/billing/id1").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.user.billing.get("id1")


@pytest.mark.asyncio
async def test_user_billing_history(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/billing/history/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.billing.history.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_billing_profile(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/billing/profile/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.billing.profile.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_billing_subscriptions(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/billing/subscriptions/id1").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.user.billing.subscriptions.get("id1")


@pytest.mark.asyncio
async def test_user_billing_subscriptions_apps(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/billing/subscriptions/apps/id1"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.billing.subscriptions.apps.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_billing_subscriptions_zones(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/billing/subscriptions/zones/id1"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.billing.subscriptions.zones.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_firewall(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/firewall/id1").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.user.firewall.get("id1")


@pytest.mark.asyncio
async def test_user_firewall_access_rules(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/firewall/access_rules/id1").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.user.firewall.access_rules.get("id1")


@pytest.mark.asyncio
async def test_user_firewall_access_rules_rules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/firewall/access_rules/rules/id1"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.firewall.access_rules.rules.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_invites(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/invites/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.invites.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_organizations(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/organizations/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.organizations.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_subscriptions(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/subscriptions/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.subscriptions.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/load_balancers/id1").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.user.load_balancers.get("id1")


@pytest.mark.asyncio
async def test_user_load_balancers_monitors(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancers/monitors/id1"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.monitors.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers_monitors_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancers/monitors/id1/preview/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.monitors.preview.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers_monitors_references(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancers/monitors/id1/references/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.monitors.references.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancers/preview/id1"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.preview.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers_pools(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/load_balancers/pools/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.pools.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers_pools_health(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancers/pools/id1/health/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.pools.health.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers_pools_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancers/pools/id1/preview/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.pools.preview.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancers_pools_references(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancers/pools/id1/references/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancers.pools.references.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_workers(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/workers/id1").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.user.workers.get("id1")


@pytest.mark.asyncio
async def test_user_workers_scripts(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/workers/scripts/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.workers.scripts.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_audit_logs(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/audit_logs/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.audit_logs.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_load_balancing_analytics(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancing_analytics/id1"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.user.load_balancing_analytics.get("id1")


@pytest.mark.asyncio
async def test_user_load_balancing_analytics_events(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/load_balancing_analytics/events/id1"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.load_balancing_analytics.events.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_tokens(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/tokens/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.tokens.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_tokens_permission_groups(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/user/tokens/permission_groups/id1"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.user.tokens.permission_groups.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_tokens_verify(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/tokens/verify/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.tokens.verify.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_user_tokens_value(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/user/tokens/id1/value/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.user.tokens.value.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_activation_check(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/activation_check/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.activation_check.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_available_plans(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/available_plans/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.available_plans.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_available_rate_plans(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/available_rate_plans/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.available_rate_plans.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_custom_certificates(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/custom_certificates/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.custom_certificates.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_custom_certificates_prioritize(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/custom_certificates/prioritize/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.custom_certificates.prioritize.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_custom_hostnames(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/custom_hostnames/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.custom_hostnames.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_custom_hostnames_fallback_origin(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/custom_hostnames/fallback_origin/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.custom_hostnames.fallback_origin.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_custom_pages(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/custom_pages/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.custom_pages.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_dns_records(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/dns_records/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.dns_records.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_dns_records_export(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/dns_records/export/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.dns_records.export.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_dns_records_import(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/dns_records/import/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.dns_records.import_.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_filters(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/filters/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.filters.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_healthchecks(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/healthchecks/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.healthchecks.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_healthchecks_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/healthchecks/preview/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.healthchecks.preview.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_keyless_certificates(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/keyless_certificates/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.keyless_certificates.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_pagerules(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/pagerules/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.pagerules.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_pagerules_settings(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/pagerules/settings/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.pagerules.settings.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_purge_cache(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/purge_cache/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.purge_cache.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_railguns(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/railguns/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.railguns.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_railguns_diagnose(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/railguns/id2/diagnose/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.railguns.diagnose.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_rulesets(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/rulesets/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.rulesets.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_rulesets_versions(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/rulesets/id2/versions/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.rulesets.versions.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_security(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/security/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.security.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_security_events(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/security/events/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.security.events.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_subscription(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/subscription/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.subscription.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_0rtt(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/0rtt/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.ortt.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_advanced_ddos(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/advanced_ddos/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.advanced_ddos.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_always_online(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/always_online/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.always_online.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_always_use_https(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/always_use_https/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.always_use_https.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_automatic_https_rewrites(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/automatic_https_rewrites/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.automatic_https_rewrites.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_brotli(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/brotli/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.brotli.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_browser_cache_ttl(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/browser_cache_ttl/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.browser_cache_ttl.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_browser_check(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/browser_check/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.browser_check.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_cache_level(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/cache_level/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.cache_level.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_challenge_ttl(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/challenge_ttl/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.challenge_ttl.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_ciphers(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/ciphers/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.ciphers.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_development_mode(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/development_mode/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.development_mode.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_email_obfuscation(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/email_obfuscation/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.email_obfuscation.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_h2_prioritization(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/h2_prioritization/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.h2_prioritization.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_hotlink_protection(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/hotlink_protection/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.hotlink_protection.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_http2(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/http2/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.http2.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_http3(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/http3/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.http3.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_image_resizing(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/image_resizing/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.image_resizing.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_ip_geolocation(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/ip_geolocation/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.ip_geolocation.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_ipv6(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/ipv6/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.ipv6.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_min_tls_version(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/min_tls_version/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.min_tls_version.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_minify(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/minify/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.minify.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_mirage(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/mirage/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.mirage.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_mobile_redirect(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/mobile_redirect/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.mobile_redirect.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_opportunistic_encryption(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/opportunistic_encryption/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.opportunistic_encryption.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_opportunistic_onion(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/opportunistic_onion/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.opportunistic_onion.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_origin_error_page_pass_thru(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/origin_error_page_pass_thru/id2"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.origin_error_page_pass_thru.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_polish(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/polish/id2"
    ).mock(  # noqa
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.polish.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_prefetch_preload(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/prefetch_preload/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.prefetch_preload.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_privacy_pass(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/privacy_pass/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.privacy_pass.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_pseudo_ipv4(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/pseudo_ipv4/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.pseudo_ipv4.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_response_buffering(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/response_buffering/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.response_buffering.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_rocket_loader(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/rocket_loader/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.rocket_loader.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_security_header(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/security_header/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.security_header.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_security_level(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/security_level/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.security_level.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_server_side_exclude(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/server_side_exclude/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.server_side_exclude.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_sort_query_string_for_cache(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/sort_query_string_for_cache/id2"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.sort_query_string_for_cache.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_ssl(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/ssl/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.ssl.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_tls_1_3(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/tls_1_3/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.tls_1_3.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_tls_client_auth(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/tls_client_auth/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.tls_client_auth.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_true_client_ip_header(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/true_client_ip_header/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.true_client_ip_header.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_waf(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/waf/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.waf.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_webp(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/settings/webp/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.webp.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_settings_websockets(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/settings/websockets/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.settings.websockets.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_analytics(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/analytics/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.analytics.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_analytics_colos(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/analytics/colos/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.analytics.colos.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_analytics_dashboard(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/analytics/dashboard/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.analytics.dashboard.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_analytics_latency(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/analytics/latency/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.analytics.latency.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_analytics_latency_colos(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/analytics/latency/colos/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.analytics.latency.colos.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/firewall/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.firewall.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_firewall_access_rules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/access_rules/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.firewall.access_rules.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_firewall_access_rules_rules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/access_rules/rules/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.access_rules.rules.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall_lockdowns(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/lockdowns/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.lockdowns.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall_rules(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/firewall/rules/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.rules.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall_ua_rules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/ua_rules/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.ua_rules.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall_waf(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/firewall/waf/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.firewall.waf.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_firewall_waf_overrides(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/waf/overrides/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.waf.overrides.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall_waf_packages(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/waf/packages/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.waf.packages.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall_waf_packages_groups(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/waf/packages/id2/groups/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.waf.packages.groups.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_firewall_waf_packages_rules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/firewall/waf/packages/id2/rules/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.firewall.waf.packages.rules.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_rate_limits(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/rate_limits/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.rate_limits.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_dns_analytics(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/dns_analytics/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.dns_analytics.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_dns_analytics_report(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/dns_analytics/report/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.dns_analytics.report.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_dns_analytics_report_bytime(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/dns_analytics/report/bytime/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.dns_analytics.report.bytime.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_amp(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/amp/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.amp.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_amp_sxg(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/amp/sxg/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.amp.sxg.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logpush(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logpush/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.logpush.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_logpush_datasets(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logpush/datasets/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.logpush.datasets.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_logpush_datasets_fields(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logpush/datasets/id2/fields/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logpush.datasets.fields.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logpush_datasets_jobs(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logpush/datasets/id2/jobs/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logpush.datasets.jobs.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logpush_jobs(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logpush/jobs/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logpush.jobs.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logpush_ownership(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logpush/ownership/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logpush.ownership.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logpush_ownership_validate(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logpush/ownership/validate/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logpush.ownership.validate.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logpush_validate(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logpush/validate/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.logpush.validate.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_logpush_validate_destination(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logpush/validate/destination/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.logpush.validate.destination.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_logpush_validate_destination_exists(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logpush/validate/destination/exists/id2"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logpush.validate.destination.exists.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logpush_validate_origin(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logpush/validate/origin/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logpush.validate.origin.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logs(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logs/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.logs.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_logs_control(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logs/control/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logs.control.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logs_control_retention(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logs/control/retention/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.logs.control.retention.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_logs_control_retention_flag(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logs/control/retention/flag/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logs.control.retention.flag.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logs_received(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logs/received/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logs.received.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logs_received_fields(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/logs/received/fields/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logs.received.fields.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_logs_rayids(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/logs/rayids/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.logs.rayids.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_argo(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/argo/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.argo.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_argo_tiered_caching(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/argo/tiered_caching/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.argo.tiered_caching.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_argo_smart_routing(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/argo/smart_routing/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.argo.smart_routing.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_dnssec(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/dnssec/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.dnssec.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_spectrum(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/spectrum/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.spectrum.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_spectrum_analytics(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/spectrum/analytics/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.spectrum.analytics.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_spectrum_analytics_aggregate(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/spectrum/analytics/aggregate/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.spectrum.analytics.aggregate.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_spectrum_analytics_aggregate_current(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/spectrum/analytics/aggregate/current/id2"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.spectrum.analytics.aggregate.current.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_spectrum_analytics_events(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/spectrum/analytics/events/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.spectrum.analytics.events.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_spectrum_analytics_events_bytime(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/spectrum/analytics/events/bytime/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.spectrum.analytics.events.bytime.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_spectrum_analytics_events_summary(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/spectrum/analytics/events/summary/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.spectrum.analytics.events.summary.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_spectrum_apps(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/spectrum/apps/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.spectrum.apps.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_ssl(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/ssl/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.ssl.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_ssl_analyze(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/ssl/analyze/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.ssl.analyze.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_ssl_certificate_packs(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/ssl/certificate_packs/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.ssl.certificate_packs.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_ssl_certificate_packs_order(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/ssl/certificate_packs/order/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.ssl.certificate_packs.order.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_ssl_certificate_packs_quota(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/ssl/certificate_packs/quota/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.ssl.certificate_packs.quota.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_ssl_verification(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/ssl/verification/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.ssl.verification.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_ssl_universal(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/ssl/universal/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.ssl.universal.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_ssl_universal_settings(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/ssl/universal/settings/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.ssl.universal.settings.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_origin_tls_client_auth(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/origin_tls_client_auth/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.origin_tls_client_auth.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_origin_tls_client_auth_hostnames(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/origin_tls_client_auth/hostnames/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.origin_tls_client_auth.hostnames.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_origin_tls_client_auth_hostnames_certificates(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/origin_tls_client_auth/hostnames/certificates/id2"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.origin_tls_client_auth.hostnames.certificates.get(
            "id1", "id2"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_origin_tls_client_auth_settings(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/origin_tls_client_auth/settings/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.origin_tls_client_auth.settings.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_workers(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/workers/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.workers.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_workers_filters(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/workers/filters/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.workers.filters.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_workers_routes(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/workers/routes/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.workers.routes.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_workers_script(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/workers/script/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.workers.script.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_workers_script_bindings(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/workers/script/bindings/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.workers.script.bindings.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_load_balancers(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/load_balancers/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.load_balancers.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_secondary_dns(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/secondary_dns/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.secondary_dns.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_secondary_dns_force_axfr(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/secondary_dns/force_axfr/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.secondary_dns.force_axfr.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_media(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/media/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.media.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_media_embed(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/media/id2/embed/id3").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.media.embed.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_media_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/media/id2/preview/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.media.preview.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/access/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.zones.access.get("id1", "id2")


@pytest.mark.asyncio
async def test_zones_access_apps(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/access/apps/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.apps.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_apps_policies(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/apps/id2/policies/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.apps.policies.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_apps_revoke_tokens(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/apps/id2/revoke_tokens/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.apps.revoke_tokens.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_certificates(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/certificates/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.certificates.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_apps_ca(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/apps/id2/ca/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.apps.ca.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_groups(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/groups/id2"
    ).mock(  # noqa
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.groups.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_identity_providers(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/identity_providers/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.identity_providers.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_organizations(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/organizations/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.organizations.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_organizations_revoke_user(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/organizations/revoke_user/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.organizations.revoke_user.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_access_service_tokens(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/access/service_tokens/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.access.service_tokens.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_waiting_rooms(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones/id1/waiting_rooms/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.waiting_rooms.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_waiting_rooms_status(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/waiting_rooms/id2/status/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.waiting_rooms.status.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_zones_waiting_rooms_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/zones/id1/waiting_rooms/preview/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.waiting_rooms.preview.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_railguns(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/railguns/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.railguns.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_railguns_zones(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/railguns/id1/zones/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.railguns.zones.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_billing(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/billing/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.billing.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_billing_profile(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/billing/profile/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.billing.profile.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_custom_pages(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/custom_pages/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.custom_pages.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_members(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/members/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.members.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_railguns(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/railguns/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.railguns.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_railguns_connections(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/railguns/id2/connections/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.railguns.connections.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_registrar(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/registrar/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.registrar.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_registrar_domains(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/registrar/domains/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.registrar.domains.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_roles(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/roles/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.roles.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_rules(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/rules/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.rules.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_rules_lists(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/rules/lists/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.rules.lists.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_rules_lists_items(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/rules/lists/id2/items/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.rules.lists.items.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_rules_lists_bulk_operations(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/rules/lists/bulk_operations/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.rules.lists.bulk_operations.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_rulesets(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/rulesets/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.rulesets.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_rulesets_versions(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/rulesets/id2/versions/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.rulesets.versions.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_rulesets_import(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/rulesets/import/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.rulesets.import_.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_storage(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/storage/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.storage.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_storage_analytics(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/storage/analytics/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.storage.analytics.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_storage_analytics_stored(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/storage/analytics/stored/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.storage.analytics.stored.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_storage_kv(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/storage/kv/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.storage.kv.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_storage_kv_namespaces(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/storage/kv/namespaces/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.storage.kv.namespaces.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_storage_kv_namespaces_bulk(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/storage/kv/namespaces/id2/bulk/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.storage.kv.namespaces.bulk.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_storage_kv_namespaces_keys(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/storage/kv/namespaces/id2/keys/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.storage.kv.namespaces.keys.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_storage_kv_namespaces_values(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/storage/kv/namespaces/id2/values/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.storage.kv.namespaces.values.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_subscriptions(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/subscriptions/id2"
    ).mock(  # noqa
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.subscriptions.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_tunnels(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/tunnels/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.tunnels.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_tunnels_connections(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/tunnels/id2/connections/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.tunnels.connections.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_virtual_dns(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/virtual_dns/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.virtual_dns.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_virtual_dns_dns_analytics(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/virtual_dns/id2/dns_analytics/id3"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.virtual_dns.dns_analytics.get("id1", "id2", "id3")


@pytest.mark.asyncio
async def test_accounts_virtual_dns_dns_analytics_report(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/virtual_dns/id2/dns_analytics/report/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.virtual_dns.dns_analytics.report.get(
            "id1", "id2", "id3"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_virtual_dns_dns_analytics_report_bytime(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/virtual_dns/id2/dns_analytics/report/bytime/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.virtual_dns.dns_analytics.report.bytime.get(
            "id1", "id2", "id3"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_workers(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/workers/id2"
    ).mock(  # noqa
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.workers.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_workers_scripts(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/workers/scripts/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.workers.scripts.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_workers_scripts_schedules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/workers/scripts/id2/schedules/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.workers.scripts.schedules.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_addressing(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/addressing/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.addressing.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_addressing_prefixes(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/addressing/prefixes/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.addressing.prefixes.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_addressing_prefixes_bgp(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/addressing/prefixes/id2/bgp/id3"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.addressing.prefixes.bgp.get("id1", "id2", "id3")


@pytest.mark.asyncio
async def test_accounts_addressing_prefixes_bgp_status(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/addressing/prefixes/id2/bgp/status/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.addressing.prefixes.bgp.status.get(
            "id1", "id2", "id3"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_addressing_prefixes_delegations(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/addressing/prefixes/id2/delegations/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.addressing.prefixes.delegations.get(
            "id1", "id2", "id3"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_audit_logs(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/audit_logs/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.audit_logs.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.load_balancers.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_load_balancers_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/preview/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.preview.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_monitors(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/monitors/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.monitors.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_monitors_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/monitors/id2/preview/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.monitors.preview.get(
            "id1", "id2", "id3"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_monitors_references(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/monitors/id2/references/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.monitors.references.get(
            "id1", "id2", "id3"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_pools(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/pools/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.pools.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_pools_health(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/pools/id2/health/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.pools.health.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_pools_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/pools/id2/preview/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.pools.preview.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_pools_references(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/pools/id2/references/id3"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.pools.references.get(
            "id1", "id2", "id3"
        )
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_regions(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/regions/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.regions.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_load_balancers_search(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/load_balancers/search/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.load_balancers.search.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_firewall(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/firewall/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.firewall.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_firewall_access_rules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/firewall/access_rules/id2"
    ).mock(return_value=httpx.Response(200))
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.firewall.access_rules.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_firewall_access_rules_rules(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/firewall/access_rules/rules/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.firewall.access_rules.rules.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_secondary_dns(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/secondary_dns/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.secondary_dns.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_secondary_dns_masters(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/secondary_dns/masters/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.secondary_dns.masters.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_secondary_dns_primaries(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/secondary_dns/primaries/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.secondary_dns.primaries.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_secondary_dns_tsigs(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/secondary_dns/tsigs/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.secondary_dns.tsigs.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/stream/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_captions(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/stream/id2/captions/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.captions.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_copy(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/stream/copy/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.copy.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_direct_upload(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/stream/direct_upload/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.direct_upload.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_embed(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/stream/id2/embed/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.embed.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_keys(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/stream/keys/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.keys.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_preview(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/stream/preview/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.preview.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_watermarks(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/stream/watermarks/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.watermarks.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_stream_webhook(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/stream/webhook/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.stream.webhook.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/access/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.access.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_access_certificates(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/certificates/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.certificates.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_groups(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/access/groups/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.groups.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_identity_providers(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/identity_providers/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.identity_providers.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_organizations(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/organizations/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.organizations.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_organizations_revoke_user(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/organizations/revoke_user/id2"  # noqa
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.organizations.revoke_user.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_service_tokens(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/service_tokens/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.service_tokens.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_logs(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/access/logs/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.access.logs.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_access_logs_access_requests(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/logs/access_requests/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.logs.access_requests.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_apps(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/access/apps/id2").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.apps.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_apps_ca(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/apps/ca/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.apps.ca.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_access_apps_revoke_tokens(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/access/apps/id2/revoke_tokens/id3"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.access.apps.revoke_tokens.get("id1", "id2", "id3")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_accounts_diagnostics(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/accounts/id1/diagnostics/id2").mock(
        return_value=httpx.Response(200)
    )
    with pytest.raises(AttributeError):
        async with Cloudflare(config=config) as cf:
            await cf.accounts.diagnostics.get("id1", "id2")


@pytest.mark.asyncio
async def test_accounts_diagnostics_traceroute(respx_mock, config):
    respx_mock.get(
        "https://api.doesnotmatter.com/accounts/id1/diagnostics/traceroute/id2"
    ).mock(return_value=httpx.Response(200))
    async with Cloudflare(config=config) as cf:
        result = await cf.accounts.diagnostics.traceroute.get("id1", "id2")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_memberships(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/memberships/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.memberships.get("id1")
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_graphql(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/graphql/id1").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:
        result = await cf.graphql.get("id1")
        assert result.status_code == 200
