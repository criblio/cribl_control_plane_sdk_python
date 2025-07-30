# Packs
(*packs*)

## Overview

Actions related to Packs

### Available Operations

* [create_packs](#create_packs) - Install Pack
* [get_packs](#get_packs) - Get info on packs
* [update_packs](#update_packs) - Upload Pack

## create_packs

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

    res = ccp_client.packs.create_packs(id="<id>", source="<value>")

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

## get_packs

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

    res = ccp_client.packs.get_packs()

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

## update_packs

Upload Pack

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

    res = ccp_client.packs.update_packs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filename`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | the file to upload                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdatePacksResponse](../../models/updatepacksresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |