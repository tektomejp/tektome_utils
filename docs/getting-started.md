# Getting Started

## Installation

You can install Tektome directly from GitHub:

```bash
pip install git+https://github.com/tektomejp/tektome_python.git@main
```

For a specific version:

```bash
pip install git+https://github.com/tektomejp/tektome_python.git@v0.3.0
```

## Basic Usage

These classes are used to convert dictionaries provided by OpenFlow input to Pydantic dataclasses with validation.

### Working with Resources

```python
from tektome import Resource

# Create a resource from a dictionary
resource_data = {
    "uuid": "123e4567-e89b-12d3-a456-426614174000",
    "kind": "resource"
}
resource = Resource(**resource_data)

# Access the data
print(resource.uuid)  # UUID object
print(resource.kind)  # "resource"

# Convert back to dict
data = resource.model_dump()
```

### Working with Context

```python
from tektome import Context

context = Context(
    api_key="your-api-key",
    base_url="https://api.example.com",
    execution_id="exec-123"
)

print(context.api_key)
print(context.base_url)
```

### Working with Collections

```python
from tektome import Resources, Projects

# Resources collection
resources = Resources(
    uuids=["123e4567-e89b-12d3-a456-426614174000"]
)

# Projects collection
projects = Projects(
    uuids=["123e4567-e89b-12d3-a456-426614174001"]
)
```

### Working with Date and DateTime

```python
from tektome import Date, DateTime

# Date
date = Date(value="2025-11-19")
print(date.value)  # "2025-11-19"
print(date.kind)   # "date"

# DateTime
dt = DateTime(value="2025-11-19T10:30:00Z")
print(dt.value)  # "2025-11-19T10:30:00Z"
print(dt.kind)   # "datetime"
```

### Using with Pydantic Validation

```python
from tektome import Resource, Context
from pydantic import validate_call

@validate_call
def process_resource(ctx: Context, resource: Resource):
    """
    This function will automatically validate that:
    - ctx is a valid Context object
    - resource is a valid Resource object
    """
    print(f"Processing resource {resource.uuid}")
    print(f"Using API key: {ctx.api_key}")
    return "Success"

# Call with valid data - works
result = process_resource(
    ctx=Context(api_key="key", base_url="url", execution_id="id"),
    resource=Resource(uuid="123e4567-e89b-12d3-a456-426614174000", kind="resource")
)

# Call with invalid data - raises ValidationError
# This will fail because kind is wrong
try:
    result = process_resource(
        ctx=Context(api_key="key", base_url="url", execution_id="id"),
        resource=Resource(uuid="123e4567-e89b-12d3-a456-426614174000", kind="invalid")
    )
except Exception as e:
    print(f"Validation error: {e}")
```

## Development Setup

To contribute or develop with Tektome:

```bash
# Clone the repository
git clone https://github.com/tektomejp/tektome_python.git
cd tektome_python

# Install dependencies
uv sync

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=tektome
```

## Next Steps

- Explore the [API Reference](api/index.md) for detailed documentation
- Check out the [Contributing Guide](contributing.md) to contribute to the project
