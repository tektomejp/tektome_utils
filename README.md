# tektome
Utilities for handling Tektome Resources

## Available Classes

- `BaseSchema` - Base class for all schemas (forbids extra fields)
- `Resource` - Single resource with UUID and kind validation
- `Resources` - Collection of resource UUIDs
- `Project` - Single project with UUID and kind validation
- `Projects` - Collection of project UUIDs
- `AttributeDefinitions` - Collection of attribute definition UUIDs
- `Context` - Execution context with API key, base URL, and execution ID
- `Date` - Date value with kind validation
- `DateTime` - DateTime value with kind validation

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/tektomejp/tektome_utils.git@main
```

## Usage

These classes are used to convert dictionary provided by openflow input to pydantic dataclass with validation.

```python
# requirements:
# git+https://github.com/tektomejp/tektome_utils.git@v0.3.0

from tektome import Resource, Context
from pydantic import validate_call

@validate_call
def main(ctx: Context, r: Resource):
    print(f"type of ctx is: {type(ctx)} with the following data available")
    print(ctx.model_dump())
    print(f"type of r is: {type(r)} with the following data available")
    print(r.model_dump())
    """
    Perform procesing here
    """
    return "data to next step"
```

## Development

To install in development mode:

```bash
git clone https://github.com/tektomejp/tektome_utils.git
cd tektome_utils
uv sync
```
