# FunctionConfSchemaRegexFilter


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `regex`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | Regex to test against                                      |
| `regex_list`                                               | List[[models.RegexList](../models/regexlist.md)]           | :heavy_minus_sign:                                         | Additional regex patterns to test against the field.       |
| `field`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | Name of the field to apply the regex on (defaults to _raw) |