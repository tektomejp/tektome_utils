# Date & DateTime

Classes for working with date and datetime values with kind validation.

## Date

The `Date` class represents a date value with automatic kind field.

::: tektome.Date
    options:
      show_source: true
      show_root_heading: true
      heading_level: 3

### Example

```python
from tektome import Date

# Create a date
date = Date(value="2025-11-19")

# Access fields
print(date.value)  # "2025-11-19"
print(date.kind)   # "date"

# Convert to dict
data = date.model_dump()
print(data)
# {'value': '2025-11-19', 'kind': 'date'}

# Convert to JSON
json_str = date.model_dump_json()
```

### Validation

The `Date` class validates:

- `value`: Must be a non-empty string
- `kind`: Automatically set to `"date"` and validated

```python
# This works - kind is automatically set
date = Date(value="2025-11-19")
print(date.kind)  # "date"

# This will fail - empty value
try:
    date = Date(value="")
except Exception as e:
    print(f"Validation error: {e}")

# This will fail - wrong kind
try:
    date = Date(value="2025-11-19", kind="datetime")
except Exception as e:
    print(f"Validation error: {e}")
```

### Use Cases

```python
from tektome import Date
from pydantic import validate_call

@validate_call
def process_date(date: Date):
    """Process a date value."""
    print(f"Processing date: {date.value}")
    # Parse the date string as needed
    from datetime import datetime
    parsed = datetime.strptime(date.value, "%Y-%m-%d")
    return parsed

# Use the function
result = process_date(Date(value="2025-11-19"))
```

## DateTime

The `DateTime` class represents a datetime value with automatic kind field.

::: tektome.DateTime
    options:
      show_source: true
      show_root_heading: true
      heading_level: 3

### Example

```python
from tektome import DateTime

# Create a datetime
dt = DateTime(value="2025-11-19T10:30:00Z")

# Access fields
print(dt.value)  # "2025-11-19T10:30:00Z"
print(dt.kind)   # "datetime"

# Convert to dict
data = dt.model_dump()
print(data)
# {'value': '2025-11-19T10:30:00Z', 'kind': 'datetime'}

# Convert to JSON
json_str = dt.model_dump_json()
```

### Validation

The `DateTime` class validates:

- `value`: Must be a non-empty string
- `kind`: Automatically set to `"datetime"` and validated

```python
# This works - kind is automatically set
dt = DateTime(value="2025-11-19T10:30:00Z")
print(dt.kind)  # "datetime"

# This will fail - empty value
try:
    dt = DateTime(value="")
except Exception as e:
    print(f"Validation error: {e}")

# This will fail - wrong kind
try:
    dt = DateTime(value="2025-11-19T10:30:00Z", kind="date")
except Exception as e:
    print(f"Validation error: {e}")
```

### Use Cases

```python
from tektome import DateTime
from pydantic import validate_call
from datetime import datetime

@validate_call
def process_datetime(dt: DateTime):
    """Process a datetime value."""
    print(f"Processing datetime: {dt.value}")
    # Parse the datetime string
    parsed = datetime.fromisoformat(dt.value.replace('Z', '+00:00'))
    return parsed

# Use the function
result = process_datetime(DateTime(value="2025-11-19T10:30:00Z"))
print(result)
```

## Date vs DateTime

Both classes follow the same pattern but have different `kind` values:

| Class | Kind Value | Typical Format |
|-------|-----------|----------------|
| `Date` | `"date"` | `"2025-11-19"` |
| `DateTime` | `"datetime"` | `"2025-11-19T10:30:00Z"` |

```python
from tektome import Date, DateTime

# Date - for day-level precision
date = Date(value="2025-11-19")

# DateTime - for timestamp precision
dt = DateTime(value="2025-11-19T10:30:00Z")

# Both have a 'kind' field for type identification
print(date.kind)    # "date"
print(dt.kind)      # "datetime"
```
