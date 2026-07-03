# PaginatedMasterWorkerEntry


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `items`                                                          | List[[models.MasterWorkerEntry](../models/masterworkerentry.md)] | :heavy_check_mark:                                               | The pre-limited items in the list of results                     |
| `count`                                                          | *int*                                                            | :heavy_check_mark:                                               | Number of items present in the items array                       |
| `offset`                                                         | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Pagination offset                                                |
| `limit`                                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Pagination limit                                                 |
| `total_count`                                                    | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Total number of items available (present when limit is set)      |