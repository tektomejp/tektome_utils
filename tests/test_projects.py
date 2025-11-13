"""Test suite for Projects class."""
import uuid
import pytest
from pydantic import ValidationError
from tektome_utils import Projects


class TestProjectsCreation:
    """Test Projects creation."""

    def test_create_projects_with_valid_data(self, sample_uuid_list):
        """Test creating Projects with valid data."""
        projects = Projects(id=sample_uuid_list, kind="project[]")
        assert projects.id == sample_uuid_list
        assert projects.kind == "project[]"
        assert len(projects.id) == 3

    def test_create_projects_with_uuid_strings(self):
        """Test creating Projects with UUID strings."""
        uuid_strings = [str(uuid.uuid4()) for _ in range(3)]
        projects = Projects(id=uuid_strings, kind="project[]")
        assert len(projects.id) == 3
        for i, uuid_obj in enumerate(projects.id):
            assert str(uuid_obj) == uuid_strings[i]

    def test_create_projects_from_dict(self, sample_uuid_list):
        """Test creating Projects from a dictionary."""
        data = {
            "id": [str(uid) for uid in sample_uuid_list],
            "kind": "project[]"
        }
        projects = Projects(**data)
        assert len(projects.id) == 3
        assert projects.kind == "project[]"

    def test_create_projects_with_empty_list(self):
        """Test creating Projects with empty list."""
        projects = Projects(id=[], kind="project[]")
        assert projects.id == []
        assert len(projects.id) == 0

    def test_create_projects_with_single_uuid(self, sample_uuid):
        """Test creating Projects with single UUID."""
        projects = Projects(id=[sample_uuid], kind="project[]")
        assert len(projects.id) == 1
        assert projects.id[0] == sample_uuid


class TestProjectsValidation:
    """Test Projects validation."""

    def test_kind_must_be_project_array(self, sample_uuid_list):
        """Test that kind must be 'project[]'."""
        with pytest.raises(ValidationError) as exc_info:
            Projects(id=sample_uuid_list, kind="project")
        assert "kind must be 'project[]'" in str(exc_info.value)

    def test_kind_cannot_be_resource_array(self, sample_uuid_list):
        """Test that kind cannot be 'resource[]'."""
        with pytest.raises(ValidationError) as exc_info:
            Projects(id=sample_uuid_list, kind="resource[]")
        assert "kind must be 'project[]'" in str(exc_info.value)

    def test_id_is_required(self):
        """Test that id field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Projects(kind="project[]")
        assert "id" in str(exc_info.value)

    def test_kind_is_required(self, sample_uuid_list):
        """Test that kind field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Projects(id=sample_uuid_list)
        assert "kind" in str(exc_info.value)

    def test_invalid_uuid_in_list(self):
        """Test that invalid UUID in list raises error."""
        with pytest.raises(ValidationError):
            Projects(id=["not-a-uuid"], kind="project[]")

    def test_mixed_valid_and_invalid_uuids(self, sample_uuid):
        """Test that mixing valid and invalid UUIDs raises error."""
        with pytest.raises(ValidationError):
            Projects(id=[sample_uuid, "invalid-uuid"], kind="project[]")

    def test_id_must_be_list(self, sample_uuid):
        """Test that id must be a list."""
        with pytest.raises(ValidationError):
            Projects(id=sample_uuid, kind="project[]")


class TestProjectsSerialization:
    """Test Projects serialization."""

    def test_model_dump(self, sample_uuid_list):
        """Test converting Projects to dictionary."""
        projects = Projects(id=sample_uuid_list, kind="project[]")
        data = projects.model_dump()
        assert data["id"] == sample_uuid_list
        assert data["kind"] == "project[]"
        assert len(data["id"]) == 3

    def test_model_dump_json(self, sample_uuid_list):
        """Test converting Projects to JSON string."""
        projects = Projects(id=sample_uuid_list, kind="project[]")
        json_str = projects.model_dump_json()
        assert "project[]" in json_str
        for uid in sample_uuid_list:
            assert str(uid) in json_str

    def test_model_dump_with_mode_json(self, sample_uuid_list):
        """Test model_dump with mode='json' serializes UUIDs as strings."""
        projects = Projects(id=sample_uuid_list, kind="project[]")
        data = projects.model_dump(mode='json')
        assert len(data["id"]) == 3
        for i, uid_str in enumerate(data["id"]):
            assert uid_str == str(sample_uuid_list[i])
            assert isinstance(uid_str, str)

    def test_model_dump_empty_list(self):
        """Test model_dump with empty list."""
        projects = Projects(id=[], kind="project[]")
        data = projects.model_dump()
        assert data["id"] == []


class TestProjectsEquality:
    """Test Projects equality."""

    def test_projects_with_same_values_are_equal(self, sample_uuid_list):
        """Test that Projects with same values are equal."""
        projects1 = Projects(id=sample_uuid_list, kind="project[]")
        projects2 = Projects(id=sample_uuid_list, kind="project[]")
        assert projects1 == projects2

    def test_projects_with_different_ids_are_not_equal(self):
        """Test that Projects with different IDs are not equal."""
        projects1 = Projects(id=[uuid.uuid4()], kind="project[]")
        projects2 = Projects(id=[uuid.uuid4()], kind="project[]")
        assert projects1 != projects2

    def test_projects_with_different_order_are_not_equal(self):
        """Test that Projects with different order are not equal."""
        uuid1, uuid2 = uuid.uuid4(), uuid.uuid4()
        projects1 = Projects(id=[uuid1, uuid2], kind="project[]")
        projects2 = Projects(id=[uuid2, uuid1], kind="project[]")
        assert projects1 != projects2

    def test_projects_not_equal_to_resources(self, sample_uuid_list):
        """Test that Projects is not equal to Resources with same IDs."""
        from tektome_utils import Resources
        projects = Projects(id=sample_uuid_list, kind="project[]")
        resources = Resources(id=sample_uuid_list, kind="resource[]")
        assert projects != resources


class TestProjectsEdgeCases:
    """Test Projects edge cases."""

    def test_large_list_of_uuids(self):
        """Test creating Projects with large list of UUIDs."""
        large_list = [uuid.uuid4() for _ in range(1000)]
        projects = Projects(id=large_list, kind="project[]")
        assert len(projects.id) == 1000

    def test_duplicate_uuids_allowed(self, sample_uuid):
        """Test that duplicate UUIDs are allowed in the list."""
        projects = Projects(id=[sample_uuid, sample_uuid], kind="project[]")
        assert len(projects.id) == 2
        assert projects.id[0] == projects.id[1]

    def test_list_type_preservation(self, sample_uuid_list):
        """Test that list type is preserved."""
        projects = Projects(id=sample_uuid_list, kind="project[]")
        assert isinstance(projects.id, list)
        for uid in projects.id:
            assert isinstance(uid, uuid.UUID)


class TestProjectsValidateCall:
    """Test Projects with validate_call decorator."""

    def test_validate_call_with_dict(self, sample_uuid_list):
        """Test that validate_call converts dict to Projects."""
        from pydantic import validate_call

        @validate_call
        def process_projects(projects: Projects):
            return projects

        result = process_projects(
            projects={
                "id": [str(uid) for uid in sample_uuid_list],
                "kind": "project[]"
            }
        )
        assert isinstance(result, Projects)
        assert len(result.id) == 3
        assert result.kind == "project[]"

    def test_validate_call_with_projects_instance(self, sample_uuid_list):
        """Test that validate_call accepts Projects directly."""
        from pydantic import validate_call

        @validate_call
        def process_projects(projects: Projects):
            return projects

        projects = Projects(id=sample_uuid_list, kind="project[]")
        result = process_projects(projects=projects)
        assert isinstance(result, Projects)
        assert len(result.id) == 3
