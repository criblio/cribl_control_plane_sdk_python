# PipelineFunctionUnrollConf


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `src_expr`                                                                            | *str*                                                                                 | :heavy_check_mark:                                                                    | Field in which to find/calculate the array to unroll. Example: _raw, _raw.split(/\n/) |
| `dst_field`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | Field in destination event in which to place the unrolled value                       |