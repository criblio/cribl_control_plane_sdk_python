# S3AwsAuthenticationMethodSecretPartitioningScheme

Partitioning scheme used for this dataset. Using a known scheme like DDSS enables more efficient data reading and retrieval.

## Example Usage

```python
from cribl_control_plane.models import S3AwsAuthenticationMethodSecretPartitioningScheme

value = S3AwsAuthenticationMethodSecretPartitioningScheme.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `NONE` | none   |
| `DDSS` | ddss   |