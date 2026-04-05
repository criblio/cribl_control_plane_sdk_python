# Git

Git status of the Worker Group, Outpost Group, or Edge Fleet configuration. Automatically populated and returned in responses.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `commit`                                                      | *Optional[str]*                                               | :heavy_minus_sign:                                            | Commit hash of the currently committed configuration version. |
| `local_changes`                                               | *Optional[int]*                                               | :heavy_minus_sign:                                            | Number of local configuration changes not yet committed.      |
| `log`                                                         | List[[models.Commit](../models/commit.md)]                    | :heavy_minus_sign:                                            | List of recent configuration commits.                         |