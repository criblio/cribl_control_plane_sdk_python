# DNSLookupField


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `in_field_name`                                                                    | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `resource_record_type`                                                             | [Optional[models.ResourceRecordType]](../models/resourcerecordtype.md)             | :heavy_minus_sign:                                                                 | The DNS record type (RR) to return. Defaults to 'A'.                               |
| `out_field_name`                                                                   | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Name of field to add lookup results to. Leave blank to overwrite the lookup field. |