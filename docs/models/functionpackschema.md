# FunctionPackSchema


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `unpacked_fields`                                      | List[*str*]                                            | :heavy_check_mark:                                     | List of fields to keep, everything else will be packed |
| `target`                                               | *Optional[str]*                                        | :heavy_minus_sign:                                     | Name of the (packed) target field                      |