# FunctionConfSchemaGrok


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `pattern`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Grok pattern to extract fields. Syntax supported: %{PATTERN_NAME:FIELD_NAME} |
| `pattern_list`                                                               | List[[models.PatternList](../models/patternlist.md)]                         | :heavy_minus_sign:                                                           | N/A                                                                          |
| `source`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Field on which to perform Grok extractions                                   |