# ObjectACLOptions

Object ACL to assign to uploaded objects

## Example Usage

```python
from cribl_control_plane.models import ObjectACLOptions

value = ObjectACLOptions.PRIVATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `PRIVATE`                   | private                     |
| `PUBLIC_READ`               | public-read                 |
| `PUBLIC_READ_WRITE`         | public-read-write           |
| `AUTHENTICATED_READ`        | authenticated-read          |
| `AWS_EXEC_READ`             | aws-exec-read               |
| `BUCKET_OWNER_READ`         | bucket-owner-read           |
| `BUCKET_OWNER_FULL_CONTROL` | bucket-owner-full-control   |