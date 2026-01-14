# FunctionConfSchemaMvExpand


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `source_fields`                                                    | List[*str*]                                                        | :heavy_minus_sign:                                                 | Array of property-/field-names to expand                           |
| `target_names`                                                     | List[*str*]                                                        | :heavy_minus_sign:                                                 | stores the value as new target field name                          |
| `row_limit`                                                        | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | max. number of rows generated out of every source events           |
| `item_index_name`                                                  | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | name of an optional index property generated into the output       |
| `bag_expansion_mode`                                               | [Optional[models.BagExpansionMode]](../models/bagexpansionmode.md) | :heavy_minus_sign:                                                 | decides if bag-values are expanded to bags or arrays               |