# Block


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `header`                                       | *str*                                          | :heavy_check_mark:                             | N/A                                            |
| `lines`                                        | List[[models.DiffLine](../models/diffline.md)] | :heavy_check_mark:                             | Diff Line                                      |
| `new_start_line`                               | *float*                                        | :heavy_check_mark:                             | N/A                                            |
| `old_start_line`                               | *float*                                        | :heavy_check_mark:                             | N/A                                            |
| `old_start_line2`                              | *Optional[float]*                              | :heavy_minus_sign:                             | N/A                                            |