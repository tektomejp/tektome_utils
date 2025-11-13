# tektome_utils
Utilities for handling Tektome Resources

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/tektomejp/tektome_utils.git@main
```

## Usage

These classes are used to convert dictionary provided by openflow input to pydantic dataclass with validation.

```python
from tektome_utils import Resource
from pydantic import validate_call


@validate_call  # validate_call attempts to convert input dict to Resource class
def main(resource: Resource):
    print(f"resource is of type: {type(resource)}")  # resource is of type: <class '....Resource'>
    return {"data": "some data"}
```

## Development

To install in development mode:

```bash
git clone https://github.com/tektomejp/tektome_utils.git
cd tektome_utils
pip install -e .
```
