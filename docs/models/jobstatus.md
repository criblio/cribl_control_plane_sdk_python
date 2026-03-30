# JobStatus

Status of a job, including its current state and failure reason.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `reason`                                                                                 | Dict[str, *Any*]                                                                         | :heavy_minus_sign:                                                                       | Reason the job entered its current <code>state</code>, typically populated upon failure. |
| `state`                                                                                  | [models.State](../models/state.md)                                                       | :heavy_check_mark:                                                                       | State of the Job                                                                         |