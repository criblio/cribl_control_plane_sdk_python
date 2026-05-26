# StatusType

Runtime status: health, metrics, and optional persistent-queue info. Fields may be absent when data is unavailable.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `error`                                                                | [Optional[models.StatusError]](../models/statuserror.md)               | :heavy_minus_sign:                                                     | N/A                                                                    |
| `health`                                                               | [Optional[models.HealthStringType]](../models/healthstringtype.md)     | :heavy_minus_sign:                                                     | N/A                                                                    |
| `metrics`                                                              | Dict[str, *Any*]                                                       | :heavy_minus_sign:                                                     | Metrics data for the Source or Destination.                            |
| `pq`                                                                   | [Optional[models.WorkerPQStatus]](../models/workerpqstatus.md)         | :heavy_minus_sign:                                                     | N/A                                                                    |
| `timestamp`                                                            | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | Timestamp (in Unix time) when the status was last updated.             |
| `use_status_from_lb`                                                   | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Set to prefer status from the LB process, not from the worker process. |