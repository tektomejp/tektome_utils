"""Test suite for Resources class."""
import uuid
import pytest
from pydantic import ValidationError
from tektome_utils import Resources


class TestResourcesCreation:
    """Test Resources creation."""

    def test_create_resources_with_valid_data(self, sample_uuid_list):
        """Test creating Resources with valid data."""
        resources = Resources(id=sample_uuid_list, kind="resource[]")
        assert resources.id == sample_uuid_list
        assert resources.kind == "resource[]"
        assert len(resources.id) == 3

    def test_create_resources_with_uuid_strings(self):
        """Test creating Resources with UUID strings."""
        uuid_strings = [str(uuid.uuid4()) for _ in range(3)]
        resources = Resources(id=uuid_strings, kind="resource[]")
        assert len(resources.id) == 3
        for i, uuid_obj in enumerate(resources.id):
            assert str(uuid_obj) == uuid_strings[i]

    def test_create_resources_from_dict(self, sample_uuid_list):
        """Test creating Resources from a dictionary."""
        data = {
            "id": [str(uid) for uid in sample_uuid_list],
            "kind": "resource[]"
        }
        resources = Resources(**data)
        assert len(resources.id) == 3
        assert resources.kind == "resource[]"

    def test_create_resources_with_empty_list(self):
        """Test creating Resources with empty list."""
        resources = Resources(id=[], kind="resource[]")
        assert resources.id == []
        assert len(resources.id) == 0

    def test_create_resources_with_single_uuid(self, sample_uuid):
        """Test creating Resources with single UUID."""
        resources = Resources(id=[sample_uuid], kind="resource[]")
        assert len(resources.id) == 1
        assert resources.id[0] == sample_uuid


class TestResourcesValidation:
    """Test Resources validation."""

    def test_kind_must_be_resource_array(self, sample_uuid_list):
        """Test that kind must be 'resource[]'."""
        with pytest.raises(ValidationError) as exc_info:
            Resources(id=sample_uuid_list, kind="resource")
        assert "kind must be 'resource[]'" in str(exc_info.value)

    def test_kind_cannot_be_wrong_array(self, sample_uuid_list):
        """Test that kind cannot be a different array type."""
        with pytest.raises(ValidationError) as exc_info:
            Resources(id=sample_uuid_list, kind="project[]")
        assert "kind must be 'resource[]'" in str(exc_info.value)

    def test_id_is_required(self):
        """Test that id field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Resources(kind="resource[]")
        assert "id" in str(exc_info.value)

    def test_kind_is_required(self, sample_uuid_list):
        """Test that kind field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Resources(id=sample_uuid_list)
        assert "kind" in str(exc_info.value)

    def test_invalid_uuid_in_list(self):
        """Test that invalid UUID in list raises error."""
        with pytest.raises(ValidationError):
            Resources(id=["not-a-uuid"], kind="resource[]")

    def test_mixed_valid_and_invalid_uuids(self, sample_uuid):
        """Test that mixing valid and invalid UUIDs raises error."""
        with pytest.raises(ValidationError):
            Resources(id=[sample_uuid, "invalid-uuid"], kind="resource[]")

    def test_id_must_be_list(self, sample_uuid):
        """Test that id must be a list."""
        with pytest.raises(ValidationError):
            Resources(id=sample_uuid, kind="resource[]")


class TestResourcesSerialization:
    """Test Resources serialization."""

    def test_model_dump(self, sample_uuid_list):
        """Test converting Resources to dictionary."""
        resources = Resources(id=sample_uuid_list, kind="resource[]")
        data = resources.model_dump()
        assert data["id"] == sample_uuid_list
        assert data["kind"] == "resource[]"
        assert len(data["id"]) == 3

    def test_model_dump_json(self, sample_uuid_list):
        """Test converting Resources to JSON string."""
        resources = Resources(id=sample_uuid_list, kind="resource[]")
        json_str = resources.model_dump_json()
        assert "resource[]" in json_str
        for uid in sample_uuid_list:
            assert str(uid) in json_str

    def test_model_dump_with_mode_json(self, sample_uuid_list):
        """Test model_dump with mode='json' serializes UUIDs as strings."""
        resources = Resources(id=sample_uuid_list, kind="resource[]")
        data = resources.model_dump(mode='json')
        assert len(data["id"]) == 3
        for i, uid_str in enumerate(data["id"]):
            assert uid_str == str(sample_uuid_list[i])
            assert isinstance(uid_str, str)

    def test_model_dump_empty_list(self):
        """Test model_dump with empty list."""
        resources = Resources(id=[], kind="resource[]")
        data = resources.model_dump()
        assert data["id"] == []


class TestResourcesEquality:
    """Test Resources equality."""

    def test_resources_with_same_values_are_equal(self, sample_uuid_list):
        """Test that Resources with same values are equal."""
        resources1 = Resources(id=sample_uuid_list, kind="resource[]")
        resources2 = Resources(id=sample_uuid_list, kind="resource[]")
        assert resources1 == resources2

    def test_resources_with_different_ids_are_not_equal(self):
        """Test that Resources with different IDs are not equal."""
        resources1 = Resources(id=[uuid.uuid4()], kind="resource[]")
        resources2 = Resources(id=[uuid.uuid4()], kind="resource[]")
        assert resources1 != resources2

    def test_resources_with_different_order_are_not_equal(self):
        """Test that Resources with different order are not equal."""
        uuid1, uuid2 = uuid.uuid4(), uuid.uuid4()
        resources1 = Resources(id=[uuid1, uuid2], kind="resource[]")
        resources2 = Resources(id=[uuid2, uuid1], kind="resource[]")
        assert resources1 != resources2


class TestResourcesEdgeCases:
    """Test Resources edge cases."""

    def test_large_list_of_uuids(self):
        """Test creating Resources with large list of UUIDs."""
        large_list = [uuid.uuid4() for _ in range(1000)]
        resources = Resources(id=large_list, kind="resource[]")
        assert len(resources.id) == 1000

    def test_duplicate_uuids_allowed(self, sample_uuid):
        """Test that duplicate UUIDs are allowed in the list."""
        resources = Resources(id=[sample_uuid, sample_uuid], kind="resource[]")
        assert len(resources.id) == 2
        assert resources.id[0] == resources.id[1]

    def test_list_type_preservation(self, sample_uuid_list):
        """Test that list type is preserved."""
        resources = Resources(id=sample_uuid_list, kind="resource[]")
        assert isinstance(resources.id, list)
        for uid in resources.id:
            assert isinstance(uid, uuid.UUID)
