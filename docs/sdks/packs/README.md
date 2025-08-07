# Packs
(*packs*)

## Overview

Actions related to Packs

### Available Operations

* [install](#install) - Install a Pack
* [list](#list) - List all Packs
* [delete](#delete) - Uninstall a Pack
* [update](#update) - Update a Pack

## install

Install Pack

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.install(id="<id>", source="<value>", allow_custom_functions=False, author="<value>", description="premeditation coincide although", display_name="Myah14", exports=[
        "<value 1>",
    ], force=False, inputs=4076.64, min_log_stream_version="<value>", outputs=2759.4, spec="<value>", tags={
        "data_type": [],
        "domain": [],
        "streamtags": [
            "<value 1>",
            "<value 2>",
        ],
        "technology": [
            "<value 1>",
        ],
    }, version="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `source`                                                                    | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `allow_custom_functions`                                                    | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | N/A                                                                         |
| `author`                                                                    | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `description`                                                               | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `display_name`                                                              | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `exports`                                                                   | List[*str*]                                                                 | :heavy_minus_sign:                                                          | N/A                                                                         |
| `force`                                                                     | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | N/A                                                                         |
| `inputs`                                                                    | *Optional[float]*                                                           | :heavy_minus_sign:                                                          | N/A                                                                         |
| `min_log_stream_version`                                                    | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `outputs`                                                                   | *Optional[float]*                                                           | :heavy_minus_sign:                                                          | N/A                                                                         |
| `spec`                                                                      | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `tags`                                                                      | [Optional[models.PackRequestBodyTags]](../../models/packrequestbodytags.md) | :heavy_minus_sign:                                                          | N/A                                                                         |
| `version`                                                                   | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.CreatePacksResponse](../../models/createpacksresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list

Get info on packs

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.list(with_="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `with_`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma separated list of entities, "outputs", "inputs"               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPacksResponse](../../models/getpacksresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Uninstall Pack from the system

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Pack name                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletePacksByIDResponse](../../models/deletepacksbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Upgrade Pack

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.update(id="<id>", source="<value>", minor="<value>", spec="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Pack name                                                           |
| `source`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | body string required Pack source                                    |
| `minor`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | body boolean optional Only upgrade to minor/patch versions          |
| `spec`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | body string optional Specify a branch, tag or a semver spec         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdatePacksByIDResponse](../../models/updatepacksbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |