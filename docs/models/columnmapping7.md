# ColumnMapping7


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `column_name`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | Name of the column in ClickHouse that will store field value                |
| `column_type`                                                               | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Type of the column in the ClickHouse database                               |
| `column_value_expression`                                                   | *str*                                                                       | :heavy_check_mark:                                                          | JavaScript expression to compute value to be inserted into ClickHouse table |