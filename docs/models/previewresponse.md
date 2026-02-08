# PreviewResponse


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `count`                                                    | *float*                                                    | :heavy_check_mark:                                         | Total count of captured events.                            |
| `items`                                                    | List[[models.CapturedEvent](../models/capturedevent.md)]   | :heavy_check_mark:                                         | Array of events captured during Pipeline preview.          |
| `message`                                                  | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `profile`                                                  | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `stats`                                                    | [Optional[models.CaptureStats]](../models/capturestats.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `stderr`                                                   | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |