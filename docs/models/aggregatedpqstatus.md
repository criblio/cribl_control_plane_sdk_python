# AggregatedPQStatus


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `error`                                                                     | [Optional[models.StatusError]](../models/statuserror.md)                    | :heavy_minus_sign:                                                          | N/A                                                                         |
| `health`                                                                    | [models.Health](../models/health.md)                                        | :heavy_check_mark:                                                          | Health status of the persistent queue.                                      |
| `health_counts`                                                             | [models.HealthCountType](../models/healthcounttype.md)                      | :heavy_check_mark:                                                          | N/A                                                                         |
| `timestamp`                                                                 | *int*                                                                       | :heavy_check_mark:                                                          | Timestamp (in Unix time) when the persistent queue status was last updated. |