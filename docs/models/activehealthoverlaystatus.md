# ActiveHealthOverlayStatus


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `binary_version`                                           | *str*                                                      | :heavy_check_mark:                                         | Binary version targeted by the active overlay.             | 4.12.0                                                     |
| `overlay_id`                                               | *str*                                                      | :heavy_check_mark:                                         | Active overlay identifier.                                 | **Example 1:** patch.0<br/>**Example 2:** sideload.a1b2c3d |
| `state`                                                    | *Literal["active"]*                                        | :heavy_check_mark:                                         | Current overlay state.                                     | active                                                     |