# PipelineFunctionGeoipAdditionalField


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `extra_in_field`                                             | *str*                                                        | :heavy_check_mark:                                           | Field name in which to find an IP to look up. Can be nested. |
| `extra_out_field`                                            | *str*                                                        | :heavy_check_mark:                                           | Field name in which to store the GeoIP lookup results        |