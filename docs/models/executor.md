# Executor


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `type`                                                                             | *str*                                                                              | :heavy_check_mark:                                                                 | The type of executor to run                                                        |
| `store_task_results`                                                               | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Determines whether or not to write task results to disk                            |
| `conf`                                                                             | [Optional[models.ExecutorSpecificSettings]](../models/executorspecificsettings.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |