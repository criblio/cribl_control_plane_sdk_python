# ListMasterWorkerEntryRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `filter_exp`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Filter expression evaluated against nodes                            |
| `sort`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Sorting object (JSON stringified) expression evaluated against nodes |
| `sort_exp`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Sorting expression evaluated against nodes                           |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Maximum number of nodes to return                                    |
| `offset`                                                             | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Pagination offset                                                    |
| `filter_`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Filter object (JSON stringified) to select nodes                     |