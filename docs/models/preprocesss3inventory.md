# PreprocessS3Inventory


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `disabled`                                                                   | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `command`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Command to feed the data through (via stdin) and process its output (stdout) |
| `args`                                                                       | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Arguments to be added to the custom command                                  |