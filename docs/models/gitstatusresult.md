# GitStatusResult


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `ahead`                                      | *float*                                      | :heavy_check_mark:                           | N/A                                          |
| `behind`                                     | *float*                                      | :heavy_check_mark:                           | N/A                                          |
| `conflicted`                                 | List[*str*]                                  | :heavy_check_mark:                           | N/A                                          |
| `created`                                    | List[*str*]                                  | :heavy_check_mark:                           | N/A                                          |
| `current`                                    | *str*                                        | :heavy_check_mark:                           | N/A                                          |
| `deleted`                                    | List[*str*]                                  | :heavy_check_mark:                           | N/A                                          |
| `files`                                      | List[[models.File](../models/file.md)]       | :heavy_check_mark:                           | N/A                                          |
| `modified`                                   | List[*str*]                                  | :heavy_check_mark:                           | N/A                                          |
| `not_added`                                  | List[*str*]                                  | :heavy_check_mark:                           | N/A                                          |
| `renamed`                                    | List[[models.Renamed](../models/renamed.md)] | :heavy_check_mark:                           | N/A                                          |
| `staged`                                     | List[*str*]                                  | :heavy_check_mark:                           | N/A                                          |