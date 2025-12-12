# SimplePivotConfiguration


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `label_field`                                 | *Optional[str]*                               | :heavy_minus_sign:                            | Fields to be used for the left-most column.   |
| `data_fields`                                 | List[*str*]                                   | :heavy_minus_sign:                            | Fields with the cell values (i.e. aggregates) |
| `qualifier_fields`                            | List[*str*]                                   | :heavy_minus_sign:                            | Fields to qualify or group data fields        |