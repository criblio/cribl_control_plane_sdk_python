# HBLeaderInfo

Connection parameters for the Leader Node, as reported in a Worker heartbeat.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `host`                                                          | *str*                                                           | :heavy_check_mark:                                              | Leader hostname or IP address.                                  |
| `port`                                                          | *int*                                                           | :heavy_check_mark:                                              | Leader TCP port.                                                |
| `servername`                                                    | *Optional[str]*                                                 | :heavy_minus_sign:                                              | TLS server name (SNI) for the Leader connection.                |
| `tls`                                                           | *Optional[bool]*                                                | :heavy_minus_sign:                                              | If <code>true</code>, TLS is enabled for the Leader connection. |