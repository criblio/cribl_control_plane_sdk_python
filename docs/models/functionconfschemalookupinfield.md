# FunctionConfSchemaLookupInField


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `event_field`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | Field name as it appears in events                                                      |
| `lookup_field`                                                                          | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Optional: The field name as it appears in the lookup file. Defaults to event field name |