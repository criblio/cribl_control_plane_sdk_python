# FunctionConfSchemaSamplingRule


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `filter_`                                                                          | *str*                                                                              | :heavy_check_mark:                                                                 | JavaScript filter expression matching events to be sampled. Use true to match all. |
| `rate`                                                                             | *int*                                                                              | :heavy_check_mark:                                                                 | Sampling rate; picks one out of N matching events                                  |