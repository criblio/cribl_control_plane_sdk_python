# DistinctConfiguration


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `group_by`                                                             | List[*str*]                                                            | :heavy_minus_sign:                                                     | Defines the properties that are concatenated to produce distinct key   |
| `max_combinations`                                                     | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | maximum number of tracked combinations                                 |
| `max_depth`                                                            | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | maximum number of groupBy properties                                   |
| `is_federated`                                                         | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | indicator that the operator runs on a federated executor               |
| `suppress_previews`                                                    | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Toggle this on to suppress generating previews of intermediate results |