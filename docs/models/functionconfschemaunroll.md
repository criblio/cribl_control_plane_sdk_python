# FunctionConfSchemaUnroll


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `src_expr`                                                                            | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Field in which to find/calculate the array to unroll. Example: _raw, _raw.split(/\n/) |
| `dst_field`                                                                           | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Field in destination event in which to place the unrolled value                       |