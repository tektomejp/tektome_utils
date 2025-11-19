# BaseSchema

The `BaseSchema` class is the base class for all Tektome schemas. It provides common configuration and validation behavior.

::: tektome.BaseSchema
    options:
      show_source: true
      show_root_heading: true
      heading_level: 2

## Features

- **Extra Fields Forbidden**: Prevents accidental data corruption by rejecting unexpected fields
- **Pydantic Integration**: Built on Pydantic for robust validation and serialization
- **Inheritance**: All Tektome classes inherit from this base class

## Example

```python
from tektome import BaseSchema

# BaseSchema is typically used as a parent class
# All Tektome classes inherit its behavior

# For example, this will raise a validation error:
from tektome import Resource

try:
    resource = Resource(
        uuid="123e4567-e89b-12d3-a456-426614174000",
        kind="resource",
        extra_field="not allowed"  # This will fail!
    )
except Exception as e:
    print(f"Validation error: {e}")
```

## Configuration

The `BaseSchema` class uses Pydantic's `ConfigDict` with the following settings:

- `extra="forbid"`: Reject any fields not defined in the model
