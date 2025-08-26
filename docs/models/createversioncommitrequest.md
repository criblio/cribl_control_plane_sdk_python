# CreateVersionCommitRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `group_id`                                                                        | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | The <code>id</code> of the Worker Group or Edge Fleet to create a new commit for. |
| `git_commit_params`                                                               | [models.GitCommitParams](../models/gitcommitparams.md)                            | :heavy_check_mark:                                                                | GitCommitParams object                                                            |