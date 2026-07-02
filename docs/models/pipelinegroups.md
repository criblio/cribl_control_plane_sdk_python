# PipelineGroups


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `name`                                                                               | *str*                                                                                | :heavy_check_mark:                                                                   | Name of the group.                                                                   |
| `description`                                                                        | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Brief description of the group.                                                      |
| `disabled`                                                                           | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | If <code>true</code>, disable all items in the group. Otherwise, <code>false</code>. |