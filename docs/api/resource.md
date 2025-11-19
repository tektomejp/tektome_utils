# Resource & Resources

Classes for working with individual resources and collections of resources.

## Resource

The `Resource` class represents a single Tektome resource with UUID and kind validation.

::: tektome.Resource
    options:
      show_source: true
      show_root_heading: true
      heading_level: 3

### Example

```python
from tektome import Resource
from uuid import UUID

# Create a resource
resource = Resource(
    uuid="123e4567-e89b-12d3-a456-426614174000",
    kind="resource"
)

# Access fields
print(resource.uuid)  # UUID object
print(resource.kind)  # "resource"

# Convert to dict
data = resource.model_dump()
print(data)
# {'uuid': UUID('123e4567-e89b-12d3-a456-426614174000'), 'kind': 'resource'}

# Convert to JSON
json_str = resource.model_dump_json()
```

### Validation

The `Resource` class validates:

- `uuid`: Must be a valid UUID (automatically converted from string)
- `kind`: Must be exactly `"resource"`

```python
# This will fail - invalid kind
try:
    resource = Resource(
        uuid="123e4567-e89b-12d3-a456-426614174000",
        kind="invalid"
    )
except Exception as e:
    print(f"Validation error: {e}")

# This will fail - invalid UUID
try:
    resource = Resource(
        uuid="not-a-uuid",
        kind="resource"
    )
except Exception as e:
    print(f"Validation error: {e}")
```

## Resources

The `Resources` class represents a collection of resource UUIDs.

::: tektome.Resources
    options:
      show_source: true
      show_root_heading: true
      heading_level: 3

### Example

```python
from tektome import Resources

# Create a collection of resources
resources = Resources(
    uuids=[
        "123e4567-e89b-12d3-a456-426614174000",
        "123e4567-e89b-12d3-a456-426614174001",
        "123e4567-e89b-12d3-a456-426614174002"
    ]
)

# Access UUIDs
for uuid in resources.uuids:
    print(uuid)  # Each is a UUID object

# Convert to dict
data = resources.model_dump()
```

### Validation

The `Resources` class validates:

- `uuids`: Must be a list of valid UUIDs (automatically converted from strings)

```python
# This will fail - invalid UUID in list
try:
    resources = Resources(
        uuids=["123e4567-e89b-12d3-a456-426614174000", "not-a-uuid"]
    )
except Exception as e:
    print(f"Validation error: {e}")
```
