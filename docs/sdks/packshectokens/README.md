# Packs.Sources.HecTokens

## Overview

### Available Operations

* [create](#create) - Add an HEC token and optional metadata to a Splunk HEC Source within a Pack
* [update](#update) - Update metadata for an HEC token for a Splunk HEC Source within a Pack

## create

Add an HEC token and optional metadata to the specified Splunk HEC Source within the specified Pack.

### Example Usage: HecTokenExamplesHecToken

<!-- UsageSnippet language="python" operationID="createInputSystemHecTokenByPackAndId" method="post" path="/p/{pack}/system/inputs/{id}/hectoken" example="HecTokenExamplesHecToken" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.hec_tokens.create(id="<id>", pack="<value>", token="12345678901", enabled=True, metadata=[
        {
            "name": "fieldX",
            "value": "valueX",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: HecTokenExamplesHecTokenWithIndexAccess

<!-- UsageSnippet language="python" operationID="createInputSystemHecTokenByPackAndId" method="post" path="/p/{pack}/system/inputs/{id}/hectoken" example="HecTokenExamplesHecTokenWithIndexAccess" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.hec_tokens.create(id="<id>", pack="<value>", token="12345678901", allowed_indexes_at_token=[
        "myIndex6",
    ], enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                     | Type                                                                                                                                                                                                          | Required                                                                                                                                                                                                      | Description                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                            | The <code>id</code> of the Splunk HEC Source.                                                                                                                                                                 |
| `pack`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                            | The <code>id</code> of the Pack to create.                                                                                                                                                                    |
| `token`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                            | The HEC token value to add to the Splunk HEC Source.                                                                                                                                                          |
| `allowed_indexes_at_token`                                                                                                                                                                                    | List[*str*]                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                            | List of index names that the HEC token is allowed to write to.                                                                                                                                                |
| `description`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                            | Brief description for the HEC token.                                                                                                                                                                          |
| `enabled`                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                            | If <code>true</code>, the HEC token is enabled. Otherwise, <code>false</code>.                                                                                                                                |
| `metadata`                                                                                                                                                                                                    | List[[models.EventBreakerRuleFields](../../models/eventbreakerrulefields.md)]                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                            | Array of key-value pairs to associate with the HEC token for tagging, categorization, or providing additional context. Each item in the array is an object with a <code>name</code> and a <code>value</code>. |
| `retries`                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                           |

### Response

**[models.CountedInputSplunkHec](../../models/countedinputsplunkhec.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the metadata for the specified HEC token for the specified Splunk HEC Source within the specified Pack.

### Example Usage: HecTokenExamplesHecToken

<!-- UsageSnippet language="python" operationID="updateInputSystemHecTokenByPackAndIdAndToken" method="patch" path="/p/{pack}/system/inputs/{id}/hectoken/{token}" example="HecTokenExamplesHecToken" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.hec_tokens.update(id="<id>", token="<value>", pack="<value>", enabled=True, metadata=[
        {
            "name": "fieldX",
            "value": "valueX",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: HecTokenExamplesHecTokenWithIndexAccess

<!-- UsageSnippet language="python" operationID="updateInputSystemHecTokenByPackAndIdAndToken" method="patch" path="/p/{pack}/system/inputs/{id}/hectoken/{token}" example="HecTokenExamplesHecTokenWithIndexAccess" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.packs.sources.hec_tokens.update(id="<id>", token="<value>", pack="<value>", allowed_indexes_at_token=[
        "myIndex6",
    ], enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                     | Type                                                                                                                                                                                                          | Required                                                                                                                                                                                                      | Description                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                            | The <code>id</code> of the Splunk HEC Source.                                                                                                                                                                 |
| `token`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                            | The HEC token value to update.                                                                                                                                                                                |
| `pack`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                            | The <code>id</code> of the Pack to update.                                                                                                                                                                    |
| `allowed_indexes_at_token`                                                                                                                                                                                    | List[*str*]                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                            | List of index names that the HEC token is allowed to write to.                                                                                                                                                |
| `description`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                            | Brief description for the HEC token.                                                                                                                                                                          |
| `enabled`                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                            | If <code>true</code>, the HEC token is enabled. Otherwise, <code>false</code>.                                                                                                                                |
| `metadata`                                                                                                                                                                                                    | List[[models.EventBreakerRuleFields](../../models/eventbreakerrulefields.md)]                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                            | Array of key-value pairs to associate with the HEC token for tagging, categorization, or providing additional context. Each item in the array is an object with a <code>name</code> and a <code>value</code>. |
| `retries`                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                           |

### Response

**[models.CountedInputSplunkHec](../../models/countedinputsplunkhec.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |