# Project & Projects

Classes for working with individual projects and collections of projects.

## Project

The `Project` class represents a single Tektome project with UUID and kind validation.

::: tektome.Project
    options:
      show_source: true
      show_root_heading: true
      heading_level: 3

### Example

```python
from tektome import Project
from uuid import UUID

# Create a project
project = Project(
    uuid="123e4567-e89b-12d3-a456-426614174000",
    kind="project"
)

# Access fields
print(project.uuid)  # UUID object
print(project.kind)  # "project"

# Convert to dict
data = project.model_dump()
print(data)
# {'uuid': UUID('123e4567-e89b-12d3-a456-426614174000'), 'kind': 'project'}

# Convert to JSON
json_str = project.model_dump_json()
```

### Validation

The `Project` class validates:

- `uuid`: Must be a valid UUID (automatically converted from string)
- `kind`: Must be exactly `"project"`

```python
# This will fail - invalid kind
try:
    project = Project(
        uuid="123e4567-e89b-12d3-a456-426614174000",
        kind="invalid"
    )
except Exception as e:
    print(f"Validation error: {e}")

# This will fail - invalid UUID
try:
    project = Project(
        uuid="not-a-uuid",
        kind="project"
    )
except Exception as e:
    print(f"Validation error: {e}")
```

## Projects

The `Projects` class represents a collection of project UUIDs.

::: tektome.Projects
    options:
      show_source: true
      show_root_heading: true
      heading_level: 3

### Example

```python
from tektome import Projects

# Create a collection of projects
projects = Projects(
    uuids=[
        "123e4567-e89b-12d3-a456-426614174000",
        "123e4567-e89b-12d3-a456-426614174001",
        "123e4567-e89b-12d3-a456-426614174002"
    ]
)

# Access UUIDs
for uuid in projects.uuids:
    print(uuid)  # Each is a UUID object

# Convert to dict
data = projects.model_dump()
```

### Validation

The `Projects` class validates:

- `uuids`: Must be a list of valid UUIDs (automatically converted from strings)

```python
# This will fail - invalid UUID in list
try:
    projects = Projects(
        uuids=["123e4567-e89b-12d3-a456-426614174000", "not-a-uuid"]
    )
except Exception as e:
    print(f"Validation error: {e}")
```
