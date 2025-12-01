# Cribl
(*system.settings.cribl*)

## Overview

### Available Operations

* [list](#list) - Get Cribl system settings
* [update](#update) - Update Cribl system settings

## list

Get Cribl system settings

### Example Usage

<!-- UsageSnippet language="python" operationID="getSystemSettingsConf" method="get" path="/system/settings/conf" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.settings.cribl.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSystemSettingsConf](../../models/countedsystemsettingsconf.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update Cribl system settings

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSystemSettingsConf" method="patch" path="/system/settings/conf" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.settings.cribl.update(api={
        "base_url": "https://both-draw.com/",
        "disable_api_cache": True,
        "disabled": False,
        "headers": {

        },
        "host": "meaty-spring.biz",
        "idle_session_ttl": 89.27,
        "listen_on_port": True,
        "login_rate_limit": "<value>",
        "port": 2424.38,
        "protocol": "<value>",
        "scripts": True,
        "sensitive_fields": [
            "<value 1>",
            "<value 2>",
        ],
        "ssl": {
            "ca_path": "<value>",
            "cert_path": "<value>",
            "disabled": True,
            "passphrase": "<value>",
            "priv_key_path": "<value>",
        },
        "sso_rate_limit": "<value>",
        "worker_remote_access": True,
    }, backups={
        "backup_persistence": "<value>",
        "backups_directory": "<value>",
    }, custom_logo={
        "enabled": False,
        "logo_description": "<value>",
        "logo_image": "<value>",
    }, pii={
        "enable_pii_detection": False,
    }, proxy={
        "use_env_vars": True,
    }, rollback={
        "rollback_enabled": False,
        "rollback_retries": 3174.73,
        "rollback_timeout": 1506.54,
    }, shutdown={
        "drain_timeout": 3723.75,
    }, sni={
        "disable_sni_routing": False,
    }, system={
        "intercom": False,
        "upgrade": models.Upgrade.API,
    }, tls={
        "default_cipher_list": "<value>",
        "default_ecdh_curve": "<value>",
        "max_version": "<value>",
        "min_version": "<value>",
        "reject_unauthorized": True,
    }, upgrade_group_settings={
        "is_rolling": False,
        "quantity": 7915.07,
        "retry_count": 4414.66,
        "retry_delay": 4374.4,
    }, upgrade_settings={
        "automatic_upgrade_check_period": "<value>",
        "disable_automatic_upgrade": False,
        "enable_legacy_edge_upgrade": False,
        "package_urls": [
            {
                "package_hash_url": "https://thrifty-teammate.net/",
                "package_url": "https://skeletal-dwell.info/",
            },
        ],
        "upgrade_source": "<value>",
    }, workers={
        "count": 2124.14,
        "enable_heap_snapshots": True,
        "load_throttle_perc": 2538.71,
        "memory": 20.53,
        "minimum": 6157.83,
        "startup_max_conns": 4731.29,
        "startup_throttle_timeout": 1613.48,
        "v8_single_thread": True,
    }, sockets={
        "directory": "/usr/ports",
    }, support={
        "feature_flag_overrides": [
            {
                "disabled": True,
                "flag_id": "<id>",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `api`                                                                         | [models.API](../../models/api.md)                                             | :heavy_check_mark:                                                            | N/A                                                                           |
| `backups`                                                                     | [models.BackupsSettingsUnion](../../models/backupssettingsunion.md)           | :heavy_check_mark:                                                            | N/A                                                                           |
| `custom_logo`                                                                 | [models.CustomLogo](../../models/customlogo.md)                               | :heavy_check_mark:                                                            | N/A                                                                           |
| `pii`                                                                         | [models.PiiSettingsUnion](../../models/piisettingsunion.md)                   | :heavy_check_mark:                                                            | N/A                                                                           |
| `proxy`                                                                       | [models.Proxy](../../models/proxy.md)                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `rollback`                                                                    | [models.RollbackSettingsUnion](../../models/rollbacksettingsunion.md)         | :heavy_check_mark:                                                            | N/A                                                                           |
| `shutdown`                                                                    | [models.Shutdown](../../models/shutdown.md)                                   | :heavy_check_mark:                                                            | N/A                                                                           |
| `sni`                                                                         | [models.SniSettingsUnion](../../models/snisettingsunion.md)                   | :heavy_check_mark:                                                            | N/A                                                                           |
| `system`                                                                      | [models.SystemSettingsConfSystem](../../models/systemsettingsconfsystem.md)   | :heavy_check_mark:                                                            | N/A                                                                           |
| `tls`                                                                         | [models.TLSSettingsUnion](../../models/tlssettingsunion.md)                   | :heavy_check_mark:                                                            | N/A                                                                           |
| `upgrade_group_settings`                                                      | [models.UpgradeGroupSettingsUnion](../../models/upgradegroupsettingsunion.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `upgrade_settings`                                                            | [models.UpgradeSettings](../../models/upgradesettings.md)                     | :heavy_check_mark:                                                            | N/A                                                                           |
| `workers`                                                                     | [models.SystemSettingsConfWorkers](../../models/systemsettingsconfworkers.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `sockets`                                                                     | [Optional[models.Sockets]](../../models/sockets.md)                           | :heavy_minus_sign:                                                            | N/A                                                                           |
| `support`                                                                     | [Optional[models.Support]](../../models/support.md)                           | :heavy_minus_sign:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CountedSystemSettingsConf](../../models/countedsystemsettingsconf.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |