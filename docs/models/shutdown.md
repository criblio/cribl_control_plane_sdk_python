# Shutdown

Graceful shutdown configuration.


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `drain_timeout`                                                                               | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | Maximum time in milliseconds to wait for in-flight events to drain before forcing a shutdown. |