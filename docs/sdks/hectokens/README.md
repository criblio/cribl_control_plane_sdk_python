# Sources.HecTokens

## Overview

### Available Operations

* [create](#create) - Add an HEC token and optional metadata to a Splunk HEC Source
* [update](#update) - Update metadata for an HEC token for a Splunk HEC Source

## create

Add an HEC token and optional metadata to the specified Splunk HEC Source.

### Example Usage

<!-- UsageSnippet language="python" operationID="createInputHecTokenById" method="post" path="/system/inputs/{id}/hectoken" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.hec_tokens.create(id="<id>", token="12345678901", allowed_indexes_at_token=[
        "<value 1>",
    ], description="toward precedent merry vaguely across ha fooey ingratiate jealously outlying", enabled=True, metadata=[
        {
            "name": "fieldX",
            "value": "valueX",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | The <code>id</code> of the Splunk HEC Source.                                           |
| `token`                                                                                 | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `allowed_indexes_at_token`                                                              | List[*str*]                                                                             | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `description`                                                                           | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `enabled`                                                                               | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `metadata`                                                                              | List[[models.AddHecTokenRequestMetadatum](../../models/addhectokenrequestmetadatum.md)] | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.CountedInputSplunkHec](../../models/countedinputsplunkhec.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the metadata for the specified HEC token for the specified Splunk HEC Source.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateInputHecTokenByIdAndToken" method="patch" path="/system/inputs/{id}/hectoken/{token}" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.sources.hec_tokens.update(id="<id>", token="<value>", allowed_indexes_at_token=[
        "<value 1>",
    ], description="once lively fooey who though while dampen please denitrify pish", enabled=True, metadata=[
        {
            "name": "fieldX",
            "value": "valueX",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the Splunk HEC Source.                                                 |
| `token`                                                                                       | *str*                                                                                         | :heavy_check_mark:                                                                            | The <code>id</code> of the HEC token to update.                                               |
| `allowed_indexes_at_token`                                                                    | List[*str*]                                                                                   | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `description`                                                                                 | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `enabled`                                                                                     | *Optional[bool]*                                                                              | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `metadata`                                                                                    | List[[models.UpdateHecTokenRequestMetadatum](../../models/updatehectokenrequestmetadatum.md)] | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.CountedInputSplunkHec](../../models/countedinputsplunkhec.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |