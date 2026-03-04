# UpdateSavedJobByIDRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id_param`                                                             | *str*                                                                  | :heavy_check_mark:                                                     | The <code>id</code> of the Collector to update.                        |
| `cribl_pack`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The <code>id</code> of the Pack that includes the Collector to update. |
| `saved_job_create_update`                                              | [models.SavedJobCreateUpdate](../models/savedjobcreateupdate.md)       | :heavy_check_mark:                                                     | SavedJobCreateUpdate object                                            |