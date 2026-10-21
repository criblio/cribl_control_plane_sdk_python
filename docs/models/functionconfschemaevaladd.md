# FunctionConfSchemaEvalAdd


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `name`                                                          | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Name of the field to set or add to the event.                   |
| `value`                                                         | *str*                                                           | :heavy_check_mark:                                              | JavaScript expression to compute the value (can be constant)    |
| `disabled`                                                      | *Optional[bool]*                                                | :heavy_minus_sign:                                              | Set to No to disable the evaluation of an individual expression |