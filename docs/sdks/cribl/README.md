# System.Settings.Cribl

## Overview

### Available Operations

* [list](#list) - Get system settings
* [update](#update) - Update system settings

## list

Get the current Cribl system settings.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSystemSettingsConf" method="get" path="/system/settings/conf" example="GetSystemSettingsConfExamplesDefault" -->
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
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Cribl system settings.<br/><br/>This endpoint supports partial updates — provide only the top-level sections (<code>api</code>, <code>workers</code>, <code>tls</code>, <code>proxy</code>, etc.) that you want to change. Omitted top-level sections are preserved unchanged.<br/><br/><b>Important:</b> while top-level sections are optional, nested objects within a section must be complete. For example, if you include <code>api</code>, you must provide its required fields (<code>host</code> and <code>port</code>).

### Example Usage: UpdateSystemSettingsExamplesUpdateApiSettings

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
### Example Usage: UpdateSystemSettingsResponseExamplesUpdateApiSettings

<!-- UsageSnippet language="python" operationID="updateSystemSettingsConf" method="patch" path="/system/settings/conf" example="UpdateSystemSettingsResponseExamplesUpdateApiSettings" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.settings.cribl.update(backups={}, pii={}, rollback={}, sni={}, tls={})

    # Handle response
    print(res)

```
### Example Usage: authenticationFailed

<!-- UsageSnippet language="python" operationID="updateSystemSettingsConf" method="patch" path="/system/settings/conf" example="authenticationFailed" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.system.settings.cribl.update(backups={}, pii={}, rollback={}, sni={}, tls={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `api`                                                                                                 | [Optional[models.APITypeSystemSettingsConf]](../../models/apitypesystemsettingsconf.md)               | :heavy_minus_sign:                                                                                    | API server configuration for the Cribl instance.                                                      |
| `apps`                                                                                                | [Optional[models.AppsTypeSystemSettingsConf]](../../models/appstypesystemsettingsconf.md)             | :heavy_minus_sign:                                                                                    | App configuration.                                                                                    |
| `backups`                                                                                             | [Optional[models.BackupsSettingsUnion]](../../models/backupssettingsunion.md)                         | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `custom_logo`                                                                                         | [Optional[models.CustomLogoTypeSystemSettingsConf]](../../models/customlogotypesystemsettingsconf.md) | :heavy_minus_sign:                                                                                    | Custom logo configuration for the Cribl UI login page and navigation bar.                             |
| `pii`                                                                                                 | [Optional[models.PiiSettingsUnion]](../../models/piisettingsunion.md)                                 | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `proxy`                                                                                               | [Optional[models.ProxyTypeSystemSettingsConf]](../../models/proxytypesystemsettingsconf.md)           | :heavy_minus_sign:                                                                                    | HTTP proxy configuration for outbound connections.                                                    |
| `rollback`                                                                                            | [Optional[models.RollbackSettingsUnion]](../../models/rollbacksettingsunion.md)                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `shutdown`                                                                                            | [Optional[models.ShutdownTypeSystemSettingsConf]](../../models/shutdowntypesystemsettingsconf.md)     | :heavy_minus_sign:                                                                                    | Graceful shutdown configuration.                                                                      |
| `sni`                                                                                                 | [Optional[models.SniSettingsUnion]](../../models/snisettingsunion.md)                                 | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `sockets`                                                                                             | [Optional[models.SocketsTypeSystemSettingsConf]](../../models/socketstypesystemsettingsconf.md)       | :heavy_minus_sign:                                                                                    | Unix domain socket configuration.                                                                     |
| `support`                                                                                             | [Optional[models.SupportTypeSystemSettingsConf]](../../models/supporttypesystemsettingsconf.md)       | :heavy_minus_sign:                                                                                    | Support and diagnostics settings.                                                                     |
| `system`                                                                                              | [Optional[models.SystemTypeSystemSettingsConf]](../../models/systemtypesystemsettingsconf.md)         | :heavy_minus_sign:                                                                                    | System-level operational settings for the Cribl instance.                                             |
| `tls`                                                                                                 | [Optional[models.TLSSettingsUnion]](../../models/tlssettingsunion.md)                                 | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `upgrade_group_settings`                                                                              | [Optional[models.UpgradeGroupSettings]](../../models/upgradegroupsettings.md)                         | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `upgrade_settings`                                                                                    | [Optional[models.UpgradeSettings]](../../models/upgradesettings.md)                                   | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `workers`                                                                                             | [Optional[models.WorkersTypeSystemSettingsConf]](../../models/workerstypesystemsettingsconf.md)       | :heavy_minus_sign:                                                                                    | Worker Process configuration.                                                                         |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.CountedSystemSettingsConf](../../models/countedsystemsettingsconf.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |