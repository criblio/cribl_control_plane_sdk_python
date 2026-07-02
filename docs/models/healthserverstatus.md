# HealthServerStatus

Health status of the Leader or Worker Node.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `overlay`                                                                                | [models.HealthOverlayStatus](../models/healthoverlaystatus.md)                           | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `role`                                                                                   | [Optional[models.Role]](../models/role.md)                                               | :heavy_minus_sign:                                                                       | Leader Node role: <code>primary</code> or <code>standby</code>.                          |
| `start_time`                                                                             | *int*                                                                                    | :heavy_check_mark:                                                                       | Timestamp (in Unix time) when the Cribl process started.                                 |
| `status`                                                                                 | [models.HealthServerStatusStatus](../models/healthserverstatusstatus.md)                 | :heavy_check_mark:                                                                       | Health state: <code>healthy</code>, <code>standby</code>, or <code>shutting down</code>. |