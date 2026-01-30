# PreprocessType


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `disabled`                                                                   | *bool*                                                                       | :heavy_check_mark:                                                           | N/A                                                                          |
| `command`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Command to feed the data through (via stdin) and process its output (stdout) |
| `args`                                                                       | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Arguments to be added to the custom command                                  |