# ObjectStorageFilter


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `data_path_format`                                                         | [Optional[models.PathFilterDataFormat]](../models/pathfilterdataformat.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `data_type_id`                                                             | *str*                                                                      | :heavy_check_mark:                                                         | Datatype identifier that maps filtered objects to a data type definition.  |
| `filter_`                                                                  | *str*                                                                      | :heavy_check_mark:                                                         | Glob pattern for selecting files within the storage path.                  |