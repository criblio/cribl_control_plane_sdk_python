# LookupDbLookupTrueOutField


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `lookup_field`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The field name as it appears in the lookup file                      |
| `event_field`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional: Field name to add to event. Defaults to lookup field name. |
| `default_value`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional: Value to assign if lookup entry is not found               |