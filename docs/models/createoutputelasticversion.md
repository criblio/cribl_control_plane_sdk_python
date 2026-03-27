# CreateOutputElasticVersion

Optional Elasticsearch version, used to format events. If not specified, will auto-discover version.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputElasticVersion

value = CreateOutputElasticVersion.AUTO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `AUTO`  | auto    |
| `SIX`   | 6       |
| `SEVEN` | 7       |