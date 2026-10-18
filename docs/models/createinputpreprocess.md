# CreateInputPreprocess

Optional preprocessing step that pipes collected data through an external command before ingestion. Not applied when fan-out is enabled.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `disabled`                                                                   | *bool*                                                                       | :heavy_check_mark:                                                           | Disabled                                                                     |
| `command`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Command to feed the data through (via stdin) and process its output (stdout) |
| `args`                                                                       | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Arguments to be added to the custom command                                  |