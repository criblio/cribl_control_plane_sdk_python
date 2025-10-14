# UpdatePacksRequest


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `filename`                                   | *str*                                        | :heavy_check_mark:                           | Filename of the pack file to upload          |
| `request_body`                               | *Union[bytes, IO[bytes], io.BufferedReader]* | :heavy_check_mark:                           | Binary file content                          |