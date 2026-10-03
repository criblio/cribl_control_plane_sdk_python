# CreateOutputStatsDestination

Internal destination settings for batch metadata and statistics.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `url`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | URL of the database that stores batch metadata and statistics.       |
| `database`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Name of the database that stores batch metadata and statistics.      |
| `table_name`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Name of the table that stores batch metadata and statistics.         |
| `auth_type`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Authentication method for the statistics destination.                |
| `username`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Username for the statistics destination.                             |
| `sql_username`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | SQL username for the statistics destination.                         |
| `password`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Password for the statistics destination.                             |
| `wait_for_async_inserts`                                             | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether to wait for asynchronous inserts to complete.                |
| `concurrency`                                                        | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Maximum number of concurrent requests to the statistics destination. |