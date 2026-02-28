# OutputLocalSearchStorageColumnMapping


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `column_name`                                                        | *str*                                                                | :heavy_check_mark:                                                   | Name of the column that will store field value                       |
| `column_type`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Type of the column in the database                                   |
| `column_value_expression`                                            | *str*                                                                | :heavy_check_mark:                                                   | JavaScript expression to compute value to be inserted into the table |