# FormatOptionsCriblLakeDataset

Storage format used for data persisted in the Dataset.

## Example Usage

```python
from cribl_control_plane.models import FormatOptionsCriblLakeDataset

value = FormatOptionsCriblLakeDataset.DDSS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DDSS`     | ddss       |
| `JSON`     | json       |
| `NETSKOPE` | netskope   |
| `PARQUET`  | parquet    |