# Tektome Documentation

Welcome to the Tektome documentation. This library provides utilities for handling Tektome Resources with Pydantic-based validation.

## Overview

Tektome is a Python package that provides strongly-typed classes for working with Tektome resources, projects, and execution contexts. It uses Pydantic for data validation and serialization.

## Available Classes

- **`BaseSchema`** - Base class for all schemas (forbids extra fields)
- **`Resource`** - Single resource with UUID and kind validation
- **`Resources`** - Collection of resource UUIDs
- **`Project`** - Single project with UUID and kind validation
- **`Projects`** - Collection of project UUIDs
- **`AttributeDefinitions`** - Collection of attribute definition UUIDs
- **`Context`** - Execution context with API key, base URL, and execution ID
- **`Date`** - Date value with kind validation
- **`DateTime`** - DateTime value with kind validation

## Quick Example

```python
from tektome import Resource, Context
from pydantic import validate_call

@validate_call
def main(ctx: Context, r: Resource):
    print(f"type of ctx is: {type(ctx)}")
    print(ctx.model_dump())
    print(f"type of r is: {type(r)}")
    print(r.model_dump())
    return "data to next step"
```

## Features

- **Type Safety**: Built on Pydantic for robust type validation
- **UUID Validation**: Automatic validation of resource and project UUIDs
- **Kind Validation**: Ensures resources have correct type identifiers
- **Extra Field Protection**: Prevents accidental data corruption from unexpected fields
- **Clean API**: Simple, intuitive interface for working with Tektome resources

## Next Steps

- Check out the [Getting Started](getting-started.md) guide
- Browse the [API Reference](api/index.md) for detailed documentation
- Learn about [Contributing](contributing.md) to the project
