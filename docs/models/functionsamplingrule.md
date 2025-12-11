# FunctionSamplingRule


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `filter_`                                                                          | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | JavaScript filter expression matching events to be sampled. Use true to match all. |
| `rate`                                                                             | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | Sampling rate; picks one out of N matching events                                  |