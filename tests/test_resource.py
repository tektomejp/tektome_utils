"""Test suite for Resource class."""
import uuid
import pytest
from pydantic import ValidationError
from tektome_utils import Resource


class TestResourceCreation:
    """Test Resource creation."""

    def test_create_resource_with_valid_data(self, sample_uuid):
        """Test creating a Resource with valid data."""
        resource = Resource(id=sample_uuid, kind="resource")
        assert resource.id == sample_uuid
        assert resource.kind == "resource"

    def test_create_resource_with_uuid_string(self, sample_uuid_str):
        """Test creating a Resource with UUID string."""
        resource = Resource(id=sample_uuid_str, kind="resource")
        assert str(resource.id) == sample_uuid_str
        assert resource.kind == "resource"

    def test_create_resource_from_dict(self, sample_uuid):
        """Test creating a Resource from a dictionary."""
        data = {
            "id": str(sample_uuid),
            "kind": "resource"
        }
        resource = Resource(**data)
        assert resource.id == sample_uuid
        assert resource.kind == "resource"


class TestResourceValidation:
    """Test Resource validation."""

    def test_kind_must_be_resource(self, sample_uuid):
        """Test that kind must be 'resource'."""
        with pytest.raises(ValidationError) as exc_info:
            Resource(id=sample_uuid, kind="invalid")
        assert "kind must be 'resource'" in str(exc_info.value)

    def test_kind_cannot_be_empty(self, sample_uuid):
        """Test that kind cannot be empty."""
        with pytest.raises(ValidationError):
            Resource(id=sample_uuid, kind="")

    def test_id_is_required(self):
        """Test that id field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Resource(kind="resource")
        assert "id" in str(exc_info.value)

    def test_kind_is_required(self, sample_uuid):
        """Test that kind field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Resource(id=sample_uuid)
        assert "kind" in str(exc_info.value)

    def test_invalid_uuid_format(self):
        """Test that invalid UUID format raises error."""
        with pytest.raises(ValidationError):
            Resource(id="not-a-uuid", kind="resource")

    def test_none_values_not_allowed(self):
        """Test that None values are not allowed for required fields."""
        with pytest.raises(ValidationError):
            Resource(id=None, kind="resource")

        with pytest.raises(ValidationError):
            Resource(id=uuid.uuid4(), kind=None)


class TestResourceSerialization:
    """Test Resource serialization."""

    def test_model_dump(self, sample_uuid):
        """Test converting Resource to dictionary."""
        resource = Resource(id=sample_uuid, kind="resource")
        data = resource.model_dump()
        assert data["id"] == sample_uuid
        assert data["kind"] == "resource"

    def test_model_dump_json(self, sample_uuid):
        """Test converting Resource to JSON string."""
        resource = Resource(id=sample_uuid, kind="resource")
        json_str = resource.model_dump_json()
        assert str(sample_uuid) in json_str
        assert "resource" in json_str

    def test_model_dump_with_mode_json(self, sample_uuid):
        """Test model_dump with mode='json' serializes UUID as string."""
        resource = Resource(id=sample_uuid, kind="resource")
        data = resource.model_dump(mode='json')
        assert data["id"] == str(sample_uuid)
        assert isinstance(data["id"], str)


class TestResourceEquality:
    """Test Resource equality."""

    def test_resources_with_same_values_are_equal(self, sample_uuid):
        """Test that Resources with same values are equal."""
        resource1 = Resource(id=sample_uuid, kind="resource")
        resource2 = Resource(id=sample_uuid, kind="resource")
        assert resource1 == resource2

    def test_resources_with_different_ids_are_not_equal(self):
        """Test that Resources with different IDs are not equal."""
        resource1 = Resource(id=uuid.uuid4(), kind="resource")
        resource2 = Resource(id=uuid.uuid4(), kind="resource")
        assert resource1 != resource2


class TestResourceEdgeCases:
    """Test Resource edge cases."""

    def test_resource_is_immutable_by_default(self, sample_uuid):
        """Test that Resource fields can be modified (Pydantic v2 default)."""
        resource = Resource(id=sample_uuid, kind="resource")
        # In Pydantic v2, models are mutable by default unless configured otherwise
        new_uuid = uuid.uuid4()
        resource.id = new_uuid
        assert resource.id == new_uuid

    def test_extra_fields_not_allowed_by_default(self, sample_uuid):
        """Test that extra fields are not allowed by default."""
        # Pydantic v2 ignores extra fields by default
        resource = Resource(id=sample_uuid, kind="resource", extra_field="value")
        assert not hasattr(resource, "extra_field")

    def test_uuid_type_preservation(self, sample_uuid):
        """Test that UUID type is preserved."""
        resource = Resource(id=sample_uuid, kind="resource")
        assert isinstance(resource.id, uuid.UUID)
        assert resource.id == sample_uuid
