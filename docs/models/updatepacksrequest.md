# UpdatePacksRequest


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `filename`                                   | *Optional[str]*                              | :heavy_minus_sign:                           | the file to upload                           |
| `size`                                       | *int*                                        | :heavy_check_mark:                           | Size of the pack file in bytes               |
| `request_body`                               | *Union[bytes, IO[bytes], io.BufferedReader]* | :heavy_check_mark:                           | file data                                    |