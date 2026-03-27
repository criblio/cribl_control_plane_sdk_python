# UpdateCriblLakeDatasetByLakeIDAndIDRequest


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `lake_id`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Lake that contains the Lake Dataset to update. |
| `id_param`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Lake Dataset to update.                        |
| `cribl_lake_dataset_update`                                               | [models.CriblLakeDatasetUpdate](../models/cribllakedatasetupdate.md)      | :heavy_check_mark:                                                        | CriblLakeDatasetUpdate object                                             |