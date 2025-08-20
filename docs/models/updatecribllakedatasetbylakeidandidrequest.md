# UpdateCriblLakeDatasetByLakeIDAndIDRequest


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `lake_id`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Lake that contains the Lake Dataset to update. |
| `id_param`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | The <code>id</code> of the Lake Dataset to update.                        |
| `cribl_lake_dataset`                                                      | [models.CriblLakeDataset](../models/cribllakedataset.md)                  | :heavy_check_mark:                                                        | CriblLakeDataset object                                                   |