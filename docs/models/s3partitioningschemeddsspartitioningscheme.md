# S3PartitioningSchemeDdssPartitioningScheme

Partitioning scheme used for this dataset. Using a known scheme like DDSS enables more efficient data reading and retrieval.

## Example Usage

```python
from cribl_control_plane.models import S3PartitioningSchemeDdssPartitioningScheme

value = S3PartitioningSchemeDdssPartitioningScheme.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `NONE` | none   |
| `DDSS` | ddss   |