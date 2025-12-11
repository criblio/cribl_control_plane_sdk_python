# FunctionOtlpLogsSchema


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `drop_non_log_events`                                            | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | N/A                                                              |
| `batch_otlp_logs`                                                | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Batch OTLP log records by shared top-level `resource` attributes |