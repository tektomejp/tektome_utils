"""Shared fixtures for tests."""
import uuid
import pytest


@pytest.fixture
def sample_uuid():
    """Return a sample UUID for testing."""
    return uuid.uuid4()


@pytest.fixture
def sample_uuid_str():
    """Return a sample UUID string for testing."""
    return str(uuid.uuid4())


@pytest.fixture
def sample_uuid_list():
    """Return a list of sample UUIDs for testing."""
    return [uuid.uuid4() for _ in range(3)]
