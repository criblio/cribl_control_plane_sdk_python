# System.Settings.Cribl

## Overview

### Available Operations

* [list](#list) - Get Cribl system settings
* [update](#update) - Update Cribl system settings

## list

Get Cribl system settings.

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

Update Cribl system settings.

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
        "disabled": False,
        "host": "meaty-spring.biz",
        "port": 2424.38,
    }, backups={
        "backup_persistence": "<value>",
        "backups_directory": "<value>",
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
        "upgrade": models.UpgradeOptionsSystemSettingsConfSystem.API,
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
    }, upgrade_settings={}, workers={
        "count": 2124.14,
        "memory": 20.53,
        "minimum": 6157.83,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `api`                                                                                                 | [models.APITypeSystemSettingsConf](../../models/apitypesystemsettingsconf.md)                         | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `backups`                                                                                             | [models.BackupsSettingsUnion](../../models/backupssettingsunion.md)                                   | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `pii`                                                                                                 | [models.PiiSettingsUnion](../../models/piisettingsunion.md)                                           | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `proxy`                                                                                               | [models.ProxyTypeSystemSettingsConf](../../models/proxytypesystemsettingsconf.md)                     | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `rollback`                                                                                            | [models.RollbackSettingsUnion](../../models/rollbacksettingsunion.md)                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `shutdown`                                                                                            | [models.ShutdownTypeSystemSettingsConf](../../models/shutdowntypesystemsettingsconf.md)               | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `sni`                                                                                                 | [models.SniSettingsUnion](../../models/snisettingsunion.md)                                           | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `system`                                                                                              | [models.SystemTypeSystemSettingsConf](../../models/systemtypesystemsettingsconf.md)                   | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `tls`                                                                                                 | [models.TLSSettingsUnion](../../models/tlssettingsunion.md)                                           | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `upgrade_group_settings`                                                                              | [models.UpgradeGroupSettingsUnion](../../models/upgradegroupsettingsunion.md)                         | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `upgrade_settings`                                                                                    | [models.UpgradeSettings](../../models/upgradesettings.md)                                             | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `workers`                                                                                             | [models.WorkersTypeSystemSettingsConf](../../models/workerstypesystemsettingsconf.md)                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `custom_logo`                                                                                         | [Optional[models.CustomLogoTypeSystemSettingsConf]](../../models/customlogotypesystemsettingsconf.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `sockets`                                                                                             | [Optional[models.SocketsTypeSystemSettingsConf]](../../models/socketstypesystemsettingsconf.md)       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `support`                                                                                             | [Optional[models.SupportTypeSystemSettingsConf]](../../models/supporttypesystemsettingsconf.md)       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.CountedSystemSettingsConf](../../models/countedsystemsettingsconf.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |