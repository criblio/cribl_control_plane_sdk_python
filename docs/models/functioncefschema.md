# FunctionCefSchema


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `output_field`                                            | *Optional[str]*                                           | :heavy_minus_sign:                                        | The field to which the CEF formatted event will be output |
| `header`                                                  | List[[models.Header](../models/header.md)]                | :heavy_minus_sign:                                        | Set of header key/value pairs                             |
| `extension`                                               | List[[models.Extension](../models/extension.md)]          | :heavy_minus_sign:                                        | Set of extension key-value pairs                          |