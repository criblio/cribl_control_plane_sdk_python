# GitRevertResult


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `audit`                                                                                   | [models.Audit](../models/audit.md)                                                        | :heavy_check_mark:                                                                        | Audit record for the revert operation, including the commit hash and affected files.      |
| `reverted`                                                                                | *bool*                                                                                    | :heavy_check_mark:                                                                        | If <code>true</code>, the revert was applied successfully. Otherwise, <code>false</code>. |