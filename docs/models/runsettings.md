# RunSettings


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `max_task_reschedule`                                                | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Maximum number of times a task can be rescheduled.                   |
| `now`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `reschedule_dropped_tasks`                                           | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Reschedule tasks that failed with non-fatal errors.                  |
| `task_heartbeat_period`                                              | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  |
| `type`                                                               | [Optional[models.RunType]](../models/runtype.md)                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `__pydantic_extra__`                                                 | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |