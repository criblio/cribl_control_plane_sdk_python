# PaginatedCriblLakeDataset


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `items`                                                        | List[[models.CriblLakeDataset](../models/cribllakedataset.md)] | :heavy_check_mark:                                             | the pre-limited items in the list of results                   |
| `count`                                                        | *int*                                                          | :heavy_check_mark:                                             | number of items present in the items array                     |
| `offset`                                                       | *int*                                                          | :heavy_check_mark:                                             | pagination offset                                              |
| `limit`                                                        | *int*                                                          | :heavy_check_mark:                                             | pagination limit                                               |
| `total_count`                                                  | *Optional[int]*                                                | :heavy_minus_sign:                                             | total number of items available (present when limit is set)    |