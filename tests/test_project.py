"""Test suite for Project class."""
import uuid
import pytest
from pydantic import ValidationError
from tektome_utils import Project


class TestProjectCreation:
    """Test Project creation."""

    def test_create_project_with_valid_data(self, sample_uuid):
        """Test creating a Project with valid data."""
        project = Project(id=sample_uuid, kind="project")
        assert project.id == sample_uuid
        assert project.kind == "project"

    def test_create_project_with_uuid_string(self, sample_uuid_str):
        """Test creating a Project with UUID string."""
        project = Project(id=sample_uuid_str, kind="project")
        assert str(project.id) == sample_uuid_str
        assert project.kind == "project"

    def test_create_project_from_dict(self, sample_uuid):
        """Test creating a Project from a dictionary."""
        data = {
            "id": str(sample_uuid),
            "kind": "project"
        }
        project = Project(**data)
        assert project.id == sample_uuid
        assert project.kind == "project"


class TestProjectValidation:
    """Test Project validation."""

    def test_kind_must_be_project(self, sample_uuid):
        """Test that kind must be 'project'."""
        with pytest.raises(ValidationError) as exc_info:
            Project(id=sample_uuid, kind="invalid")
        assert "kind must be 'project'" in str(exc_info.value)

    def test_kind_cannot_be_resource(self, sample_uuid):
        """Test that kind cannot be 'resource'."""
        with pytest.raises(ValidationError) as exc_info:
            Project(id=sample_uuid, kind="resource")
        assert "kind must be 'project'" in str(exc_info.value)

    def test_kind_cannot_be_empty(self, sample_uuid):
        """Test that kind cannot be empty."""
        with pytest.raises(ValidationError):
            Project(id=sample_uuid, kind="")

    def test_id_is_required(self):
        """Test that id field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Project(kind="project")
        assert "id" in str(exc_info.value)

    def test_kind_is_required(self, sample_uuid):
        """Test that kind field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Project(id=sample_uuid)
        assert "kind" in str(exc_info.value)

    def test_invalid_uuid_format(self):
        """Test that invalid UUID format raises error."""
        with pytest.raises(ValidationError):
            Project(id="not-a-uuid", kind="project")

    def test_none_values_not_allowed(self):
        """Test that None values are not allowed for required fields."""
        with pytest.raises(ValidationError):
            Project(id=None, kind="project")

        with pytest.raises(ValidationError):
            Project(id=uuid.uuid4(), kind=None)


class TestProjectSerialization:
    """Test Project serialization."""

    def test_model_dump(self, sample_uuid):
        """Test converting Project to dictionary."""
        project = Project(id=sample_uuid, kind="project")
        data = project.model_dump()
        assert data["id"] == sample_uuid
        assert data["kind"] == "project"

    def test_model_dump_json(self, sample_uuid):
        """Test converting Project to JSON string."""
        project = Project(id=sample_uuid, kind="project")
        json_str = project.model_dump_json()
        assert str(sample_uuid) in json_str
        assert "project" in json_str

    def test_model_dump_with_mode_json(self, sample_uuid):
        """Test model_dump with mode='json' serializes UUID as string."""
        project = Project(id=sample_uuid, kind="project")
        data = project.model_dump(mode='json')
        assert data["id"] == str(sample_uuid)
        assert isinstance(data["id"], str)


class TestProjectEquality:
    """Test Project equality."""

    def test_projects_with_same_values_are_equal(self, sample_uuid):
        """Test that Projects with same values are equal."""
        project1 = Project(id=sample_uuid, kind="project")
        project2 = Project(id=sample_uuid, kind="project")
        assert project1 == project2

    def test_projects_with_different_ids_are_not_equal(self):
        """Test that Projects with different IDs are not equal."""
        project1 = Project(id=uuid.uuid4(), kind="project")
        project2 = Project(id=uuid.uuid4(), kind="project")
        assert project1 != project2

    def test_project_not_equal_to_resource(self, sample_uuid):
        """Test that Project is not equal to Resource with same ID."""
        from tektome_utils import Resource
        project = Project(id=sample_uuid, kind="project")
        resource = Resource(id=sample_uuid, kind="resource")
        assert project != resource


class TestProjectEdgeCases:
    """Test Project edge cases."""

    def test_project_is_mutable_by_default(self, sample_uuid):
        """Test that Project fields can be modified (Pydantic v2 default)."""
        project = Project(id=sample_uuid, kind="project")
        new_uuid = uuid.uuid4()
        project.id = new_uuid
        assert project.id == new_uuid

    def test_extra_fields_not_allowed_by_default(self, sample_uuid):
        """Test that extra fields are not allowed by default."""
        project = Project(id=sample_uuid, kind="project", extra_field="value")
        assert not hasattr(project, "extra_field")

    def test_uuid_type_preservation(self, sample_uuid):
        """Test that UUID type is preserved."""
        project = Project(id=sample_uuid, kind="project")
        assert isinstance(project.id, uuid.UUID)
        assert project.id == sample_uuid


class TestProjectValidateCall:
    """Test Project with validate_call decorator."""

    def test_validate_call_with_dict(self, sample_uuid):
        """Test that validate_call converts dict to Project."""
        from pydantic import validate_call

        @validate_call
        def process_project(project: Project):
            return project

        result = process_project(project={"id": str(sample_uuid), "kind": "project"})
        assert isinstance(result, Project)
        assert result.id == sample_uuid
        assert result.kind == "project"

    def test_validate_call_with_project_instance(self, sample_uuid):
        """Test that validate_call accepts Project directly."""
        from pydantic import validate_call

        @validate_call
        def process_project(project: Project):
            return project

        project = Project(id=sample_uuid, kind="project")
        result = process_project(project=project)
        assert isinstance(result, Project)
        assert result.id == sample_uuid
