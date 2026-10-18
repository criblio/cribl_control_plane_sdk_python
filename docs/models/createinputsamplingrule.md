# CreateInputSamplingRule


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `service`                                                        | *str*                                                            | :heavy_check_mark:                                               | Datadog service name                                             |
| `environment`                                                    | *str*                                                            | :heavy_check_mark:                                               | Datadog environment name (example: prod, staging)                |
| `rate`                                                           | *float*                                                          | :heavy_check_mark:                                               | Sampling rate for this service/environment combination (0.0–1.0) |