# OutputResponseWizDefendSourceType

The Wiz log source type. Select a predefined type or enter a custom value.

## Example Usage

```python
from cribl_control_plane.models import OutputResponseWizDefendSourceType

value = OutputResponseWizDefendSourceType.AWS_CLOUDTRAIL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `AWS_CLOUDTRAIL`          | AWS_CLOUDTRAIL            |
| `AWS_EKS_AUDIT_LOGS`      | AWS_EKS_AUDIT_LOGS        |
| `AWS_RESOLVER_QUERY_LOGS` | AWS_RESOLVER_QUERY_LOGS   |
| `AZURE_ACTIVITY_LOGS`     | AZURE_ACTIVITY_LOGS       |
| `GCP_AUDIT_LOGS`          | GCP_AUDIT_LOGS            |
| `GITHUB_AUDIT_LOGS`       | GITHUB_AUDIT_LOGS         |
| `OCI_AUDIT_LOGS`          | OCI_AUDIT_LOGS            |
| `AWS_VPC_FLOW_LOGS`       | AWS_VPC_FLOW_LOGS         |