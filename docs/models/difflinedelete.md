# DiffLineDelete

Deleted line in a Git diff hunk.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `type`                                                          | [models.DiffLineDeleteType](../models/difflinedeletetype.md)    | :heavy_check_mark:                                              | Line change type. Always <code>delete</code> for deleted lines. |
| `old_number`                                                    | *int*                                                           | :heavy_check_mark:                                              | Line number in the original file.                               |
| `content`                                                       | *str*                                                           | :heavy_check_mark:                                              | Full content of the line, including the diff prefix character.  |