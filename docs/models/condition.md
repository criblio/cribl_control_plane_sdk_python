# Condition


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `key`                                              | *str*                                              | :heavy_check_mark:                                 | Event field name to match against                  |
| `operator`                                         | [models.Operator](../models/operator.md)           | :heavy_check_mark:                                 | Comparison operator                                |
| `value`                                            | [models.Value](../models/value.md)                 | :heavy_check_mark:                                 | Value to compare against (string, number, boolean) |