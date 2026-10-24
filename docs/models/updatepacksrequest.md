# UpdatePacksRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `filename`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | Filename of the Pack file to upload.                                          |
| `request_body`                                                                | *Union[bytes, IO[bytes], io.IOBase]*                                          | :heavy_check_mark:                                                            | Binary contents of the <code>.crbl</code> Pack file to stage for installation |