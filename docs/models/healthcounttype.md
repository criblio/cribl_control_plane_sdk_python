# HealthCountType


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `green`                                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Number of Worker Processes reporting a healthy (Green) status.   |
| `red`                                                            | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Number of Worker Processes reporting a critical (Red) status.    |
| `unknown`                                                        | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Number of Worker Processes reporting an unknown health status.   |
| `yellow`                                                         | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Number of Worker Processes reporting a degraded (Yellow) status. |