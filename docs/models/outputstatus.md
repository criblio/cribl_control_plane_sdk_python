# OutputStatus

Status of a Destination, aggregated across all Worker Processes.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier of the Source or Destination.                                        |
| `status`                                                                               | [models.AggregatedInputOutputStatusBody](../models/aggregatedinputoutputstatusbody.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `type`                                                                                 | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Type of the Source or Destination.                                                     |