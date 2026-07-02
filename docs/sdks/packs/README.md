# Packs

## Overview

Actions related to Packs

### Available Operations

* [install](#install) - Install a Pack
* [list](#list) - List all Packs
* [upload](#upload) - Upload a Pack file
* [get](#get) - Get a Pack
* [update](#update) - Upgrade a Pack
* [delete](#delete) - Uninstall a Pack

## install

Install a Pack.<br/><br/>To install an uploaded Pack, provide the <code>source</code> value from the <code>PUT /packs</code> response as the <code>source</code> parameter in the request body.<br/><br/>To install a Pack by importing from a URL, provide the direct URL location of the <code>.crbl</code> file for the Pack as the <code>source</code> parameter in the request body.<br/><br/>To install a Pack by importing from a Git repository, provide <code>git+&lt;repo-url&gt;</code> as the <code>source</code> parameter in the request body.<br/><br/>If you do not include the <code>source</code> parameter in the request body, an empty Pack is created.

### Example Usage: PackInstallExamplesEmptyPack

<!-- UsageSnippet language="python" operationID="createPacks" method="post" path="/packs" example="PackInstallExamplesEmptyPack" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.install(request={
        "id": "<id>",
        "spec": "<value>",
        "version": "<value>",
        "min_log_stream_version": "<value>",
        "display_name": "Amely_Gusikowski",
        "author": "<value>",
        "description": "crowded that truly sideboard ample yahoo gracious enraged",
        "source": "<value>",
        "tags": {
            "data_type": [
                "double",
                "boolean",
            ],
            "domain": [
                "delectable-transom.com",
                "radiant-sightseeing.info",
            ],
            "technology": [
                "<value 1>",
            ],
            "streamtags": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "allow_custom_functions": False,
        "force": True,
    })

    # Handle response
    print(res)

```
### Example Usage: PackInstallExamplesGitRepository

<!-- UsageSnippet language="python" operationID="createPacks" method="post" path="/packs" example="PackInstallExamplesGitRepository" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.install(request={
        "source": "git+https://github.com/criblio/cribl_ocsf_postprocessing",
        "allow_custom_functions": False,
    })

    # Handle response
    print(res)

```
### Example Usage: PackInstallExamplesPackDispensary

<!-- UsageSnippet language="python" operationID="createPacks" method="post" path="/packs" example="PackInstallExamplesPackDispensary" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.install(request={
        "source": "https://packs.cribl.io/dl/cribl-duo-rest-io/latest/cribl-duo-rest-io-latest.crbl",
        "allow_custom_functions": True,
        "force": True,
    })

    # Handle response
    print(res)

```
### Example Usage: PackInstallExamplesURL

<!-- UsageSnippet language="python" operationID="createPacks" method="post" path="/packs" example="PackInstallExamplesURL" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.install(request={
        "source": "https://github.com/criblpacks/cribl-palo-alto-networks/releases/download/1.1.4/cribl-palo-alto-networks-a3e5a19d-1.1.4.crbl",
        "allow_custom_functions": False,
    })

    # Handle response
    print(res)

```
### Example Usage: PackInstallExamplesUploadedFile

<!-- UsageSnippet language="python" operationID="createPacks" method="post" path="/packs" example="PackInstallExamplesUploadedFile" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.install(request={
        "id": "cribl-search-missing-logs",
        "source": "cribl-search-missing-logs-1.0.1.Do7DH5I.crbl",
        "allow_custom_functions": False,
    })

    # Handle response
    print(res)

```
### Example Usage: PackInstallResponseExamplesInstalledFromURL

<!-- UsageSnippet language="python" operationID="createPacks" method="post" path="/packs" example="PackInstallResponseExamplesInstalledFromURL" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.install(request={
        "version": "1.0.0",
        "source": "<value>",
        "tags": {
            "domain": [
                "security",
                "observability",
            ],
            "technology": [
                "aws",
                "splunk",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PackRequestBodyUnion](../../models/packrequestbodyunion.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedPackInstallInfo](../../models/countedpackinstallinfo.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get a list of all Packs.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPacks" method="get" path="/packs" example="PackListResponseExamplesPackList" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `with_`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Comma-separated list of additional properties to include in the response. When set, the response includes a count of each specified property in each Pack. Supported values: <code>inputs</code>, <code>outputs</code>, <code>collectors</code>. |
| `offset`                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Pagination offset                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Maximum number of items to return                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                              |

### Response

**[models.GetPacksResponse](../../models/getpacksresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## upload

Upload a Pack file. Returns the <code>source</code> ID needed to install the Pack with <code>POST /packs</code>, which you must call separately.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePacks" method="put" path="/packs" example="PackUploadResponseExamplesUploadedPack" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.upload(filename="example.file", request_body=open("example.file", "rb"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Filename of the Pack file to upload.                                |
| `request_body`                                                      | *Union[bytes, IO[bytes], io.IOBase]*                                | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadPackResponse](../../models/uploadpackresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Pack.

### Example Usage: PackGetResponseExamplesEmptyPack

<!-- UsageSnippet language="python" operationID="getPacksById" method="get" path="/packs/{id}" example="PackGetResponseExamplesEmptyPack" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.get(id="<id>")

    # Handle response
    print(res)

```
### Example Usage: PackGetResponseExamplesInstalledPack

<!-- UsageSnippet language="python" operationID="getPacksById" method="get" path="/packs/{id}" example="PackGetResponseExamplesInstalledPack" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Pack to get. Use the <code>id</code> field from the list response. |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.CountedPackInfo](../../models/countedpackinfo.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Upgrade the specified Pack.<br/><br/>If the Pack includes any user-modified versions of default Cribl Knowledge resources such as lookups, copy the modified files locally for safekeeping before upgrading the Pack. Copy the modified files back to the upgraded Pack after you install it with <code>POST /packs</code> to overwrite the default versions in the Pack.<br/><br/>After you upgrade the Pack, update any Routes, Pipelines, Sources, and Destinations that use the previous Pack version so that they reference the upgraded Pack.

### Example Usage: PackUpgradeExamplesUpgradeFromURL

<!-- UsageSnippet language="python" operationID="updatePacksById" method="patch" path="/packs/{id}" example="PackUpgradeExamplesUpgradeFromURL" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.update(id="<id>", source="https://github.com/criblpacks/cribl-palo-alto-networks/releases/download/1.1.4/cribl-palo-alto-networks-a3e5a19d-1.1.4.crbl")

    # Handle response
    print(res)

```
### Example Usage: PackUpgradeResponseExamplesUpgraded

<!-- UsageSnippet language="python" operationID="updatePacksById" method="patch" path="/packs/{id}" example="PackUpgradeResponseExamplesUpgraded" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.update(id="<id>", source="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                       | The <code>id</code> of the Pack to upgrade. Use the <code>id</code> field from the list response.                                                                                                                                        |
| `source`                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                       | Source of the upgraded Pack. Use the <code>source</code> value returned by <code>PUT /packs</code> for an uploaded file, or provide a direct URL to a <code>.crbl</code> file or a <code>git+&lt;repo-url&gt;</code> Git repository URL. |
| `allow_custom_functions`                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                       | If <code>true</code> or omitted, allow the Pack to use custom JavaScript functions. If <code>false</code>, reject Packs that use custom JavaScript functions.                                                                            |
| `minor`                                                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                       | If <code>true</code>, allow the upgrade to install a minor (non-breaking) version. Otherwise, <code>false</code>.                                                                                                                        |
| `spec`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                       | Semver range constraint to apply when resolving the Pack version to install.                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                      |

### Response

**[models.CountedPackInfo](../../models/countedpackinfo.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Uninstall the specified Pack.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletePacksById" method="delete" path="/packs/{id}" example="PackDeleteResponseExamplesUninstalled" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `id`                                                                                                | *str*                                                                                               | :heavy_check_mark:                                                                                  | The <code>id</code> of the Pack to uninstall. Use the <code>id</code> field from the list response. |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.CountedPackUninstallInfo](../../models/countedpackuninstallinfo.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |