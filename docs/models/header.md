# Header


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `name`                                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Name of the CEF header field. Header names are predefined by the CEF standard. |
| `value`                                                                        | *str*                                                                          | :heavy_check_mark:                                                             | JavaScript expression to compute the value (can be constant)                   |