# Collectors

## Overview

Actions related to Collectors

### Available Operations

* [list](#list) - List all Collectors
* [create](#create) - Create a Collector
* [get](#get) - Get a Collector
* [update](#update) - Update a Collector
* [delete](#delete) - Delete a Collector

## list

Get a list of all Collectors.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSavedJob" method="get" path="/lib/jobs" example="CollectorListResponseExamplesListed" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `collector_type`                                                    | [Optional[models.CollectorType]](../../models/collectortype.md)     | :heavy_minus_sign:                                                  | Filter by collector type.                                           |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Pagination offset                                                   |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSavedJobResponse](../../models/getsavedjobresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create

Create a new Collector.

### Example Usage: CollectorExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "executor": {
            "type": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesCriblLake

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesDatabase

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesDatabase" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "executor": {
            "type": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesFilesystem

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "executor": {
            "type": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesRest

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesRest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesS3

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesScript

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesScript" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesSplunk

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorResponseExamplesRestCollector

<!-- UsageSnippet language="python" operationID="createSavedJob" method="post" path="/lib/jobs" example="CollectorResponseExamplesRestCollector" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.create(request=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorAzureBlob(
            type=models.CollectorAzureBlobType.AZURE_BLOB,
            conf=models.AzureBlobAuthTypeClientCert(
                auth_type=models.AzureBlobAuthTypeClientCertAuthenticationMethod.CLIENT_CERT,
                storage_account_name="<value>",
                tenant_id="<id>",
                client_id="<id>",
                certificate=models.CertificateTypeAzureBlobAuthTypeClientCert(
                    certificate_name="<value>",
                ),
                container_name="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SavedJob](../../models/savedjob.md)                         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSavedJobResponse](../../models/countedsavedjobresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get

Get the specified Collector.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSavedJobById" method="get" path="/lib/jobs/{id}" example="CollectorResponseExamplesRestCollector" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Collector to get.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSavedJobResponse](../../models/countedsavedjobresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update

Update the specified Collector.<br/><br/>Provide a complete representation of the Collector that you want to update in the request body. This endpoint does not support partial updates. Cribl removes any omitted fields when updating the Collector.<br/><br/>Confirm that the configuration in your request body is correct before sending the request. If the configuration is incorrect, the updated Collector might not function as expected.

### Example Usage: CollectorExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesCriblLake

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesDatabase

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesDatabase" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesFilesystem

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "executor": {
            "type": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesRest

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesRest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesS3

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesScript

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesScript" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: CollectorExamplesSplunk

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorDatabase(
            type=models.CollectorDatabaseType.DATABASE,
            conf=models.DatabaseCollectorConf(
                connection_id="<id>",
                query="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: CollectorResponseExamplesRestCollector

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="CollectorResponseExamplesRestCollector" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "executor": {
            "type": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesAzureBlob

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesAzureBlob" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesCriblLake

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesCriblLake" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorSplunk(
            type=models.CollectorSplunkType.SPLUNK,
            conf=models.SplunkAuthenticationToken(
                authentication=models.SplunkAuthenticationTokenAuthentication.TOKEN,
                token="<value>",
                search_head="<value>",
                search="<value>",
                endpoint="<value>",
                output_mode=models.OutputModeOptionsSplunkCollectorConf.JSON,
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesDatabase

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesDatabase" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.SCHEDULED_SEARCH,
        "saved_query_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesFilesystem

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesFilesystem" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorSplunk(
            type=models.CollectorSplunkType.SPLUNK,
            conf=models.SplunkAuthenticationToken(
                authentication=models.SplunkAuthenticationTokenAuthentication.TOKEN,
                token="<value>",
                search_head="<value>",
                search="<value>",
                endpoint="<value>",
                output_mode=models.OutputModeOptionsSplunkCollectorConf.JSON,
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesGoogleCloudStorage

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesGoogleCloudStorage" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "executor": {
            "type": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesRest

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesRest" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorSplunk(
            type=models.CollectorSplunkType.SPLUNK,
            conf=models.SplunkAuthenticationToken(
                authentication=models.SplunkAuthenticationTokenAuthentication.TOKEN,
                token="<value>",
                search_head="<value>",
                search="<value>",
                endpoint="<value>",
                output_mode=models.OutputModeOptionsSplunkCollectorConf.JSON,
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesS3

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesS3" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job={
        "type": models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        "executor": {
            "type": "<value>",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesScript

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesScript" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorSplunk(
            type=models.CollectorSplunkType.SPLUNK,
            conf=models.SplunkAuthenticationToken(
                authentication=models.SplunkAuthenticationTokenAuthentication.TOKEN,
                token="<value>",
                search_head="<value>",
                search="<value>",
                endpoint="<value>",
                output_mode=models.OutputModeOptionsSplunkCollectorConf.JSON,
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: UpdateCollectorExamplesSplunk

<!-- UsageSnippet language="python" operationID="updateSavedJobById" method="patch" path="/lib/jobs/{id}" example="UpdateCollectorExamplesSplunk" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.update(id="<id>", saved_job=models.SavedJobCollection(
        type=models.JobTypeOptionsRunnableJobCollection.COLLECTION,
        collector=models.CollectorSplunk(
            type=models.CollectorSplunkType.SPLUNK,
            conf=models.SplunkAuthenticationToken(
                authentication=models.SplunkAuthenticationTokenAuthentication.TOKEN,
                token="<value>",
                search_head="<value>",
                search="<value>",
                endpoint="<value>",
                output_mode=models.OutputModeOptionsSplunkCollectorConf.JSON,
            ),
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Collector to update.                     |
| `saved_job`                                                         | [models.SavedJob](../../models/savedjob.md)                         | :heavy_check_mark:                                                  | SavedJob object.                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSavedJobResponse](../../models/countedsavedjobresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete

Delete the specified Collector.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSavedJobById" method="delete" path="/lib/jobs/{id}" example="CollectorResponseExamplesRestCollector" -->
```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    "https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.collectors.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The <code>id</code> of the Collector to delete.                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountedSavedJobResponse](../../models/countedsavedjobresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |