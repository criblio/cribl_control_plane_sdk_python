# ObjectACL

Object ACL to assign to uploaded objects

## Example Usage

```python
from cribl_control_plane.models import ObjectACL

value = ObjectACL.PRIVATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `PRIVATE`                   | private                     |
| `PUBLIC_READ`               | public-read                 |
| `PUBLIC_READ_WRITE`         | public-read-write           |
| `AUTHENTICATED_READ`        | authenticated-read          |
| `BUCKET_OWNER_FULL_CONTROL` | bucket-owner-full-control   |