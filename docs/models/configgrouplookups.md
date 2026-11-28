# ConfigGroupLookups


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `context`                                             | *str*                                                 | :heavy_check_mark:                                    | The Worker or Node context for the lookup deployment. |
| `lookups`                                             | List[[models.Lookup](../models/lookup.md)]            | :heavy_check_mark:                                    | List of lookup files deployed to this context.        |