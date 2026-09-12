# RestartResponse

Result of a restart request for a Worker or Edge Node.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `id`                                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | Unique identifier for the Worker or Edge Node (GUID).                                        |
| `message`                                                                                    | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | Error message if the restart request failed for this Node.                                   |
| `status`                                                                                     | [models.RestartResponseStatus](../models/restartresponsestatus.md)                           | :heavy_check_mark:                                                                           | Result of the restart request for this Node (<code>Restarting</code> or <code>Error</code>). |