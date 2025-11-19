# AttributeDefinitions

The `AttributeDefinitions` class represents a collection of attribute definition UUIDs.

::: tektome.AttributeDefinitions
    options:
      show_source: true
      show_root_heading: true
      heading_level: 2

## Example

```python
from tektome import AttributeDefinitions

# Create a collection of attribute definitions
attr_defs = AttributeDefinitions(
    uuids=[
        "123e4567-e89b-12d3-a456-426614174000",
        "123e4567-e89b-12d3-a456-426614174001",
        "123e4567-e89b-12d3-a456-426614174002"
    ]
)

# Access UUIDs
for uuid in attr_defs.uuids:
    print(uuid)  # Each is a UUID object

# Convert to dict
data = attr_defs.model_dump()
print(data)

# Convert to JSON
json_str = attr_defs.model_dump_json()
```

## Validation

The `AttributeDefinitions` class validates:

- `uuids`: Must be a list of valid UUIDs (automatically converted from strings)

```python
# This will fail - invalid UUID in list
try:
    attr_defs = AttributeDefinitions(
        uuids=["123e4567-e89b-12d3-a456-426614174000", "not-a-uuid"]
    )
except Exception as e:
    print(f"Validation error: {e}")
```

## Use Cases

Attribute definitions are typically used to specify metadata or configuration for resources:

```python
from tektome import AttributeDefinitions, Resource

# Define attribute definitions for a resource
attr_defs = AttributeDefinitions(
    uuids=[
        "attr-def-1-uuid",
        "attr-def-2-uuid"
    ]
)

# Use with a resource
resource = Resource(
    uuid="resource-uuid",
    kind="resource"
)

# Process resource with attribute definitions
def process_with_attrs(resource: Resource, attrs: AttributeDefinitions):
    print(f"Processing resource {resource.uuid}")
    print(f"With {len(attrs.uuids)} attribute definitions")
```
