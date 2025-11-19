# Contributing

Thank you for your interest in contributing to Tektome! This guide will help you get started.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/tektomejp/tektome_python.git
cd tektome_python
```

2. **Install dependencies**

```bash
uv sync
```

This will install all dependencies including development and documentation tools.

3. **Activate the virtual environment**

```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

## Running Tests

### Run all tests

```bash
uv run pytest
```

### Run with coverage

```bash
uv run pytest --cov=tektome
```

### Run specific tests

```bash
uv run pytest tests/test_resource.py
uv run pytest tests/test_resource.py::test_specific_function
```

## Documentation

### Building Documentation

The documentation is built using MkDocs with the Material theme.

```bash
# Install documentation dependencies
uv sync --group docs

# Serve documentation locally
uv run mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000/`.

### Building for Production

```bash
uv run mkdocs build
```

This creates a `site/` directory with the static documentation.

## Code Style

We use standard Python formatting and linting tools:

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all public functions and classes

### Example Code Style

```python
from typing import List
from uuid import UUID
from pydantic import ConfigDict
from tektome import BaseSchema

class Example(BaseSchema):
    """
    Example class demonstrating code style.

    Attributes:
        name: The name of the example
        values: List of example values
    """
    model_config = ConfigDict(extra="forbid")

    name: str
    values: List[str]

    def process(self) -> None:
        """Process the example values."""
        for value in self.values:
            print(f"{self.name}: {value}")
```

## Making Changes

### Workflow

1. **Create a new branch**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**

- Write code
- Add or update tests
- Update documentation if needed

3. **Run tests**

```bash
uv run pytest --cov=tektome
```

4. **Commit your changes**

```bash
git add .
git commit -m "Description of your changes"
```

5. **Push to GitHub**

```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request**

Go to GitHub and create a pull request from your branch.

## Pull Request Guidelines

- **Clear description**: Explain what your PR does and why
- **Tests**: Include tests for new functionality
- **Documentation**: Update docs if you're adding/changing features
- **Small PRs**: Keep PRs focused on a single feature or fix
- **Commit messages**: Write clear, descriptive commit messages

## Adding New Features

When adding a new schema class:

1. **Add the class** to `tektome/schema.py`
2. **Export it** in `tektome/__init__.py`
3. **Write tests** in `tests/`
4. **Add documentation** in `docs/api/`
5. **Update the navigation** in `mkdocs.yml`

### Example: Adding a New Class

```python
# In tektome/schema.py
class NewFeature(BaseSchema):
    """A new feature class."""
    model_config = ConfigDict(extra="forbid")

    value: str
    kind: Literal["new_feature"] = "new_feature"

# In tektome/__init__.py
from tektome.schema import NewFeature

__all__ = [
    # ... existing exports
    "NewFeature",
]

# In tests/test_new_feature.py
def test_new_feature():
    feature = NewFeature(value="test")
    assert feature.kind == "new_feature"
    assert feature.value == "test"
```

## Reporting Issues

If you find a bug or have a feature request:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with a clear title and description
3. **Include**:
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Python version and environment details
   - Code examples if relevant

## Questions?

If you have questions about contributing, feel free to:

- Open an issue on GitHub
- Check the [Getting Started](getting-started.md) guide
- Review the [API Reference](api/index.md)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
