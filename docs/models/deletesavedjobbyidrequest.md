# DeleteSavedJobByIDRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | The <code>id</code> of the Collector to delete.                                |
| `cribl_pack`                                                                   | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The <code>id</code> of the Pack that includes the Collector to delete.         |
| `group_id`                                                                     | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The <code>id</code> of the Worker Group that includes the Collector to delete. |