# OutpostNodeInfo

Node information for the Outpost through which a Worker connects to the Leader.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `groupname`                                               | *Optional[str]*                                           | :heavy_minus_sign:                                        | Name of the Outpost Group that contains the Outpost Node. |
| `guid`                                                    | *str*                                                     | :heavy_check_mark:                                        | Unique identifier for the Outpost Node.                   |
| `host`                                                    | *str*                                                     | :heavy_check_mark:                                        | Hostname or IP address for the Outpost Node.              |