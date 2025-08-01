# UpdatePacksRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `filename`                                                           | *str*                                                                | :heavy_check_mark:                                                   | the file to upload                                                   |
| `size`                                                               | *int*                                                                | :heavy_check_mark:                                                   | Size of the pack file in bytes                                       |
| `request_body`                                                       | [models.UpdatePacksRequestBody](../models/updatepacksrequestbody.md) | :heavy_check_mark:                                                   | multipart upload of the pack file                                    |