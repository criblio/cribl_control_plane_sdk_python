# PqTypeStatus

Persistent queue status information (if persistent queue is enabled).


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `error`                                                                     | [Optional[models.ErrorTypeStatusPq]](../models/errortypestatuspq.md)        | :heavy_minus_sign:                                                          | Error information for the persistent queue, if applicable.                  |
| `health`                                                                    | [models.HealthStringType](../models/healthstringtype.md)                    | :heavy_check_mark:                                                          | N/A                                                                         |
| `health_counts`                                                             | [models.HealthCountType](../models/healthcounttype.md)                      | :heavy_check_mark:                                                          | N/A                                                                         |
| `timestamp`                                                                 | *float*                                                                     | :heavy_check_mark:                                                          | Timestamp (in Unix time) when the persistent queue status was last updated. |