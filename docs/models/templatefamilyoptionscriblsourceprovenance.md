# TemplateFamilyOptionsCriblSourceProvenance

Infrastructure-as-code family that provisioned the AWS resources (absent means cloudformation).

## Example Usage

```python
from cribl_control_plane.models import TemplateFamilyOptionsCriblSourceProvenance

value = TemplateFamilyOptionsCriblSourceProvenance.CLOUDFORMATION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `CLOUDFORMATION` | cloudformation   |
| `TERRAFORM`      | terraform        |