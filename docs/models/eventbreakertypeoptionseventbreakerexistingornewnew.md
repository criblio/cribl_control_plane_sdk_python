# EventBreakerTypeOptionsEventBreakerExistingOrNewNew

Type of event-breaking rule to apply when creating a new inline ruleset.

## Example Usage

```python
from cribl_control_plane.models import EventBreakerTypeOptionsEventBreakerExistingOrNewNew

value = EventBreakerTypeOptionsEventBreakerExistingOrNewNew.REGEX

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `REGEX`          | regex            |
| `JSON`           | json             |
| `JSON_ARRAY`     | json_array       |
| `HEADER`         | header           |
| `TIMESTAMP`      | timestamp        |
| `CSV`            | csv              |
| `AWS_CLOUDTRAIL` | aws_cloudtrail   |
| `AWS_VPCFLOW`    | aws_vpcflow      |
| `AZURE_FLOWLOG`  | azure_flowlog    |