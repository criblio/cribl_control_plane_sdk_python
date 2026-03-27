# UpdateSavedJobByIDRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The <code>id</code> of the Collector to update.                        |
| `cribl_pack`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The <code>id</code> of the Pack that includes the Collector to update. |
| `saved_job`                                                            | [models.SavedJob](../models/savedjob.md)                               | :heavy_check_mark:                                                     | SavedJob object                                                        |