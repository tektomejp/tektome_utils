"""Test suite for AttributeDefinitions class."""
import uuid
import pytest
from pydantic import ValidationError
from tektome_utils import AttributeDefinitions


class TestAttributeDefinitionsCreation:
    """Test AttributeDefinitions creation."""

    def test_create_attribute_definitions_with_valid_data(self, sample_uuid_list):
        """Test creating AttributeDefinitions with valid data."""
        attr_defs = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        assert attr_defs.id == sample_uuid_list
        assert attr_defs.kind == "attribute_definition[]"
        assert len(attr_defs.id) == 3

    def test_create_attribute_definitions_with_uuid_strings(self):
        """Test creating AttributeDefinitions with UUID strings."""
        uuid_strings = [str(uuid.uuid4()) for _ in range(3)]
        attr_defs = AttributeDefinitions(id=uuid_strings, kind="attribute_definition[]")
        assert len(attr_defs.id) == 3
        for i, uuid_obj in enumerate(attr_defs.id):
            assert str(uuid_obj) == uuid_strings[i]

    def test_create_attribute_definitions_from_dict(self, sample_uuid_list):
        """Test creating AttributeDefinitions from a dictionary."""
        data = {
            "id": [str(uid) for uid in sample_uuid_list],
            "kind": "attribute_definition[]"
        }
        attr_defs = AttributeDefinitions(**data)
        assert len(attr_defs.id) == 3
        assert attr_defs.kind == "attribute_definition[]"

    def test_create_attribute_definitions_with_empty_list(self):
        """Test creating AttributeDefinitions with empty list."""
        attr_defs = AttributeDefinitions(id=[], kind="attribute_definition[]")
        assert attr_defs.id == []
        assert len(attr_defs.id) == 0

    def test_create_attribute_definitions_with_single_uuid(self, sample_uuid):
        """Test creating AttributeDefinitions with single UUID."""
        attr_defs = AttributeDefinitions(id=[sample_uuid], kind="attribute_definition[]")
        assert len(attr_defs.id) == 1
        assert attr_defs.id[0] == sample_uuid


class TestAttributeDefinitionsValidation:
    """Test AttributeDefinitions validation."""

    def test_kind_must_be_attribute_definition_array(self, sample_uuid_list):
        """Test that kind must be 'attribute_definition[]'."""
        with pytest.raises(ValidationError) as exc_info:
            AttributeDefinitions(id=sample_uuid_list, kind="resource[]")
        assert "kind must be 'attribute_definition[]'" in str(exc_info.value)

    def test_kind_cannot_be_project_array(self, sample_uuid_list):
        """Test that kind cannot be 'project[]'."""
        with pytest.raises(ValidationError) as exc_info:
            AttributeDefinitions(id=sample_uuid_list, kind="project[]")
        assert "kind must be 'attribute_definition[]'" in str(exc_info.value)

    def test_kind_cannot_be_singular(self, sample_uuid_list):
        """Test that kind cannot be singular form."""
        with pytest.raises(ValidationError) as exc_info:
            AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition")
        assert "kind must be 'attribute_definition[]'" in str(exc_info.value)

    def test_id_is_required(self):
        """Test that id field is required."""
        with pytest.raises(ValidationError) as exc_info:
            AttributeDefinitions(kind="attribute_definition[]")
        assert "id" in str(exc_info.value)

    def test_kind_is_required(self, sample_uuid_list):
        """Test that kind field is required."""
        with pytest.raises(ValidationError) as exc_info:
            AttributeDefinitions(id=sample_uuid_list)
        assert "kind" in str(exc_info.value)

    def test_invalid_uuid_in_list(self):
        """Test that invalid UUID in list raises error."""
        with pytest.raises(ValidationError):
            AttributeDefinitions(id=["not-a-uuid"], kind="attribute_definition[]")

    def test_mixed_valid_and_invalid_uuids(self, sample_uuid):
        """Test that mixing valid and invalid UUIDs raises error."""
        with pytest.raises(ValidationError):
            AttributeDefinitions(id=[sample_uuid, "invalid-uuid"], kind="attribute_definition[]")

    def test_id_must_be_list(self, sample_uuid):
        """Test that id must be a list."""
        with pytest.raises(ValidationError):
            AttributeDefinitions(id=sample_uuid, kind="attribute_definition[]")


class TestAttributeDefinitionsSerialization:
    """Test AttributeDefinitions serialization."""

    def test_model_dump(self, sample_uuid_list):
        """Test converting AttributeDefinitions to dictionary."""
        attr_defs = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        data = attr_defs.model_dump()
        assert data["id"] == sample_uuid_list
        assert data["kind"] == "attribute_definition[]"
        assert len(data["id"]) == 3

    def test_model_dump_json(self, sample_uuid_list):
        """Test converting AttributeDefinitions to JSON string."""
        attr_defs = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        json_str = attr_defs.model_dump_json()
        assert "attribute_definition[]" in json_str
        for uid in sample_uuid_list:
            assert str(uid) in json_str

    def test_model_dump_with_mode_json(self, sample_uuid_list):
        """Test model_dump with mode='json' serializes UUIDs as strings."""
        attr_defs = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        data = attr_defs.model_dump(mode='json')
        assert len(data["id"]) == 3
        for i, uid_str in enumerate(data["id"]):
            assert uid_str == str(sample_uuid_list[i])
            assert isinstance(uid_str, str)

    def test_model_dump_empty_list(self):
        """Test model_dump with empty list."""
        attr_defs = AttributeDefinitions(id=[], kind="attribute_definition[]")
        data = attr_defs.model_dump()
        assert data["id"] == []


class TestAttributeDefinitionsEquality:
    """Test AttributeDefinitions equality."""

    def test_attribute_definitions_with_same_values_are_equal(self, sample_uuid_list):
        """Test that AttributeDefinitions with same values are equal."""
        attr_defs1 = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        attr_defs2 = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        assert attr_defs1 == attr_defs2

    def test_attribute_definitions_with_different_ids_are_not_equal(self):
        """Test that AttributeDefinitions with different IDs are not equal."""
        attr_defs1 = AttributeDefinitions(id=[uuid.uuid4()], kind="attribute_definition[]")
        attr_defs2 = AttributeDefinitions(id=[uuid.uuid4()], kind="attribute_definition[]")
        assert attr_defs1 != attr_defs2

    def test_attribute_definitions_with_different_order_are_not_equal(self):
        """Test that AttributeDefinitions with different order are not equal."""
        uuid1, uuid2 = uuid.uuid4(), uuid.uuid4()
        attr_defs1 = AttributeDefinitions(id=[uuid1, uuid2], kind="attribute_definition[]")
        attr_defs2 = AttributeDefinitions(id=[uuid2, uuid1], kind="attribute_definition[]")
        assert attr_defs1 != attr_defs2


class TestAttributeDefinitionsEdgeCases:
    """Test AttributeDefinitions edge cases."""

    def test_large_list_of_uuids(self):
        """Test creating AttributeDefinitions with large list of UUIDs."""
        large_list = [uuid.uuid4() for _ in range(1000)]
        attr_defs = AttributeDefinitions(id=large_list, kind="attribute_definition[]")
        assert len(attr_defs.id) == 1000

    def test_duplicate_uuids_allowed(self, sample_uuid):
        """Test that duplicate UUIDs are allowed in the list."""
        attr_defs = AttributeDefinitions(
            id=[sample_uuid, sample_uuid],
            kind="attribute_definition[]"
        )
        assert len(attr_defs.id) == 2
        assert attr_defs.id[0] == attr_defs.id[1]

    def test_list_type_preservation(self, sample_uuid_list):
        """Test that list type is preserved."""
        attr_defs = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        assert isinstance(attr_defs.id, list)
        for uid in attr_defs.id:
            assert isinstance(uid, uuid.UUID)


class TestAttributeDefinitionsValidateCall:
    """Test AttributeDefinitions with validate_call decorator."""

    def test_validate_call_with_dict(self, sample_uuid_list):
        """Test that validate_call converts dict to AttributeDefinitions."""
        from pydantic import validate_call

        @validate_call
        def process_attr_defs(attr_defs: AttributeDefinitions):
            return attr_defs

        result = process_attr_defs(
            attr_defs={
                "id": [str(uid) for uid in sample_uuid_list],
                "kind": "attribute_definition[]"
            }
        )
        assert isinstance(result, AttributeDefinitions)
        assert len(result.id) == 3
        assert result.kind == "attribute_definition[]"

    def test_validate_call_with_attribute_definitions_instance(self, sample_uuid_list):
        """Test that validate_call accepts AttributeDefinitions directly."""
        from pydantic import validate_call

        @validate_call
        def process_attr_defs(attr_defs: AttributeDefinitions):
            return attr_defs

        attr_defs = AttributeDefinitions(id=sample_uuid_list, kind="attribute_definition[]")
        result = process_attr_defs(attr_defs=attr_defs)
        assert isinstance(result, AttributeDefinitions)
        assert len(result.id) == 3


class TestAttributeDefinitionsDocumentation:
    """Test AttributeDefinitions documentation and usage."""

    def test_class_docstring_exists(self):
        """Test that class has proper documentation."""
        assert AttributeDefinitions.__doc__ is not None
        assert "definition" in AttributeDefinitions.__doc__.lower()

    def test_field_descriptions(self, sample_uuid):
        """Test that fields have proper descriptions."""
        attr_defs = AttributeDefinitions(id=[sample_uuid], kind="attribute_definition[]")
        schema = attr_defs.model_json_schema()
        assert "id" in schema["properties"]
        assert "kind" in schema["properties"]
