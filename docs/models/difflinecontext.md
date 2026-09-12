# DiffLineContext

Unchanged context line in a Git diff hunk.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `type`                                                             | [models.DiffLineContextType](../models/difflinecontexttype.md)     | :heavy_check_mark:                                                 | Line change type. Always <code>context</code> for unchanged lines. |
| `new_number`                                                       | *int*                                                              | :heavy_check_mark:                                                 | Line number in the new file.                                       |
| `old_number`                                                       | *int*                                                              | :heavy_check_mark:                                                 | Line number in the original file.                                  |
| `content`                                                          | *str*                                                              | :heavy_check_mark:                                                 | Full content of the line, including the diff prefix character.     |