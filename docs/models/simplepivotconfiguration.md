# SimplePivotConfiguration


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `label_field`                                 | *str*                                         | :heavy_check_mark:                            | Fields to be used for the left-most column.   |
| `data_fields`                                 | List[*str*]                                   | :heavy_check_mark:                            | Fields with the cell values (i.e. aggregates) |
| `qualifier_fields`                            | List[*str*]                                   | :heavy_check_mark:                            | Fields to qualify or group data fields        |