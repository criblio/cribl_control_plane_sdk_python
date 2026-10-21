# GitFilesResponse


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `commit_message`                                        | *Optional[str]*                                         | :heavy_minus_sign:                                      | Commit message of the specified commit.                 |
| `count`                                                 | *int*                                                   | :heavy_check_mark:                                      | Number of files returned.                               |
| `items`                                                 | List[[models.GitFile](../models/gitfile.md)]            | :heavy_check_mark:                                      | Array of files that changed since the specified commit. |