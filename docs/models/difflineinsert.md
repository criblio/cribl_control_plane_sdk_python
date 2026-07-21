# DiffLineInsert

Inserted line in a Git diff hunk.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `type`                                                           | [models.DiffLineInsertType](../models/difflineinserttype.md)     | :heavy_check_mark:                                               | Line change type. Always <code>insert</code> for inserted lines. |
| `new_number`                                                     | *int*                                                            | :heavy_check_mark:                                               | Line number in the new file.                                     |
| `content`                                                        | *str*                                                            | :heavy_check_mark:                                               | Full content of the line, including the diff prefix character.   |