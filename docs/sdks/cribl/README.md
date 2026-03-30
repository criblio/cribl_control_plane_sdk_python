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
    "https://api.example.com",
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

<!-- UsageSnippet language="python" operationID="updateSystemSettingsConf" method="patch" path="/system/settings/conf" example="UpdateSystemSettingsExamplesUpdateApiSettings" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.settings.cribl.update(api={
        "disabled": False,
        "host": "0.0.0.0",
        "port": 9000,
        "ssl": {
            "cert_path": "/opt/cribl/local/cribl/auth/cribl.crt",
            "disabled": False,
            "passphrase": "",
            "priv_key_path": "/opt/cribl/local/cribl/auth/cribl.key",
        },
    }, backups={
        "backup_persistence": "24h",
        "backups_directory": "$CRIBL_STATE_DIR/backups",
    }, pii={
        "enable_pii_detection": False,
    }, proxy={
        "use_env_vars": False,
    }, rollback={
        "rollback_enabled": True,
    }, shutdown={
        "drain_timeout": 10000,
    }, sni={
        "disable_sni_routing": False,
    }, system={
        "intercom": True,
        "upgrade": models.UpgradeOptionsSystemSettingsConfSystem.API,
    }, tls={
        "default_cipher_list": "DEFAULT",
        "default_ecdh_curve": "auto",
        "max_version": "TLSv1.3",
        "min_version": "TLSv1.2",
        "reject_unauthorized": True,
    }, upgrade_group_settings={
        "is_rolling": True,
        "quantity": 100,
        "retry_count": 5,
        "retry_delay": 1000,
    }, upgrade_settings={}, workers={
        "count": 0,
        "memory": 0,
        "minimum": 1,
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