# JobSettings


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `concurrent_job_limit`           | *float*                          | :heavy_check_mark:               | N/A                              |
| `concurrent_scheduled_job_limit` | *float*                          | :heavy_check_mark:               | N/A                              |
| `concurrent_system_job_limit`    | *float*                          | :heavy_check_mark:               | N/A                              |
| `concurrent_system_task_limit`   | *float*                          | :heavy_check_mark:               | N/A                              |
| `concurrent_task_limit`          | *float*                          | :heavy_check_mark:               | N/A                              |
| `disable_tasks`                  | *Optional[bool]*                 | :heavy_minus_sign:               | N/A                              |
| `finished_job_artifacts_limit`   | *float*                          | :heavy_check_mark:               | N/A                              |
| `finished_task_artifacts_limit`  | *float*                          | :heavy_check_mark:               | N/A                              |
| `job_artifacts_reaper_period`    | *str*                            | :heavy_check_mark:               | N/A                              |
| `job_timeout`                    | *str*                            | :heavy_check_mark:               | N/A                              |
| `max_task_perc`                  | *float*                          | :heavy_check_mark:               | N/A                              |
| `scheduling_policy`              | *str*                            | :heavy_check_mark:               | N/A                              |
| `task_heartbeat_period`          | *float*                          | :heavy_check_mark:               | N/A                              |
| `task_manifest_flush_period_ms`  | *float*                          | :heavy_check_mark:               | N/A                              |
| `task_manifest_max_buffer_size`  | *float*                          | :heavy_check_mark:               | N/A                              |
| `task_manifest_read_buffer_size` | *str*                            | :heavy_check_mark:               | N/A                              |
| `task_poll_timeout_ms`           | *float*                          | :heavy_check_mark:               | N/A                              |