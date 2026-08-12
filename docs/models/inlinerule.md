# InlineRule


## Fields

| Field                | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `id`                 | *str*                | :heavy_check_mark:   | Rule ID              |
| `name`               | *str*                | :heavy_check_mark:   | Rule Name            |
| `condition`          | *str*                | :heavy_check_mark:   | Condition Expression |
| `severity_id`        | *Optional[int]*      | :heavy_minus_sign:   | Severity             |
| `confidence_id`      | *Optional[int]*      | :heavy_minus_sign:   | Confidence           |
| `is_alert`           | *Optional[bool]*     | :heavy_minus_sign:   | Is Alert             |
| `message`            | *Optional[str]*      | :heavy_minus_sign:   | Message              |
| `tags`               | List[*str*]          | :heavy_minus_sign:   | N/A                  |