# ObjectACLOptionsAuthenticatedreadBucketownerfullcontrol

Object ACL to assign to uploaded objects

## Example Usage

```python
from cribl_control_plane.models import ObjectACLOptionsAuthenticatedreadBucketownerfullcontrol

value = ObjectACLOptionsAuthenticatedreadBucketownerfullcontrol.PRIVATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `PRIVATE`                   | private                     |
| `BUCKET_OWNER_READ`         | bucket-owner-read           |
| `BUCKET_OWNER_FULL_CONTROL` | bucket-owner-full-control   |
| `PROJECT_PRIVATE`           | project-private             |
| `AUTHENTICATED_READ`        | authenticated-read          |
| `PUBLIC_READ`               | public-read                 |