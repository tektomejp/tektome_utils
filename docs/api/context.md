# Context

The `Context` class represents the execution context for Tektome operations, containing API credentials and execution information.

::: tektome.Context
    options:
      show_source: true
      show_root_heading: true
      heading_level: 2

## Example

```python
from tektome import Context

# Create a context
ctx = Context(
    api_key="your-api-key-here",
    base_url="https://gateway.tektome.com",
    execution_id="exec-123-456"
)

# Access fields
print(ctx.api_key)        # "your-api-key-here"
print(ctx.base_url)       # "https://gateway.tektome.com"
print(ctx.execution_id)   # "exec-123-456"

# Convert to dict
data = ctx.model_dump()
print(data)

# Convert to JSON
json_str = ctx.model_dump_json()
```

## Fields

- **`api_key`** (str): API key for authentication
- **`base_url`** (str): Base URL for the Tektome API
- **`execution_id`** (str): Unique identifier for the current execution

## Use with Functions

The `Context` class is commonly used with Pydantic's `@validate_call` decorator:

```python
from tektome import Context, Resource
from pydantic import validate_call

@validate_call
def process_resource(ctx: Context, resource: Resource):
    """
    Process a resource using the provided context.

    Args:
        ctx: Execution context with API credentials
        resource: Resource to process

    Returns:
        Processing result
    """
    print(f"Using API: {ctx.base_url}")
    print(f"Execution ID: {ctx.execution_id}")
    print(f"Processing resource: {resource.uuid}")

    # Use context to make API calls, etc.
    return "Success"

# Call the function
result = process_resource(
    ctx=Context(
        api_key="key",
        base_url="https://gateway.tektome.com",
        execution_id="exec-001"
    ),
    resource=Resource(
        uuid="123e4567-e89b-12d3-a456-426614174000",
        kind="resource"
    )
)
```

## Validation

All fields are required and must be non-empty strings:

```python
# This will fail - missing required fields
try:
    ctx = Context(api_key="key")
except Exception as e:
    print(f"Validation error: {e}")

# This will fail - empty strings
try:
    ctx = Context(api_key="", base_url="", execution_id="")
except Exception as e:
    print(f"Validation error: {e}")
```

## Security Notes

- Never hardcode API keys in your source code
- Use environment variables or secure configuration management
- Be careful when logging or serializing `Context` objects as they contain sensitive data

```python
import os
from tektome import Context

# Good: Load from environment
ctx = Context(
    api_key=os.environ["TEKTOME_API_KEY"],
    base_url=os.environ["TEKTOME_BASE_URL"],
    execution_id=os.environ["TEKTOME_EXECUTION_ID"]
)

# When logging, be careful about exposing secrets
safe_context = {
    "base_url": ctx.base_url,
    "execution_id": ctx.execution_id
    # Don't log api_key!
}
print(safe_context)
```
