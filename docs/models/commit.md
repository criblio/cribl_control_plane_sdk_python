# Commit


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `author_email`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Email address of the commit author.                               |
| `author_name`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Name of the commit author.                                        |
| `body`                                                            | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Body of the commit message (all lines after the subject), if any. |
| `date_`                                                           | *str*                                                             | :heavy_check_mark:                                                | Date and time of the commit.                                      |
| `hash`                                                            | *str*                                                             | :heavy_check_mark:                                                | Full commit hash.                                                 |
| `message`                                                         | *str*                                                             | :heavy_check_mark:                                                | Commit message.                                                   |
| `short`                                                           | *str*                                                             | :heavy_check_mark:                                                | Abbreviated commit hash.                                          |