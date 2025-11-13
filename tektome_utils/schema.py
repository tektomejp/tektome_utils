"""Schema classes for Tektome resources and projects."""

from uuid import UUID

from pydantic import BaseModel, Field, field_validator


class Resource(BaseModel):
    """
    Represents a single resource.
    """

    id: UUID = Field(..., description="The unique identifier for the resource")
    kind: str = Field(..., description="The kind of the schema, must be 'resource")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "resource":
            raise ValueError("kind must be 'resource'")

        return v


class Resources(BaseModel):
    """
    Represents a single resource.
    """

    ids: list[UUID] = Field(..., description="The unique identifier for the resource")
    kind: str = Field(..., description="The kind of the schema, must be 'resource[]")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "resource[]":
            raise ValueError("kind must be 'resource[]'")

        return v


class Project(BaseModel):
    """
    Represents a single project.
    """

    id: UUID = Field(..., description="The unique identifier for the project")
    kind: str = Field(..., description="The kind of the schema, must be 'project'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "project":
            raise ValueError("kind must be 'project'")

        return v


class Projects(BaseModel):
    """
    Represents a single project.
    """

    ids: list[UUID] = Field(..., description="The unique identifier for the project")
    kind: str = Field(..., description="The kind of the schema, must be 'project[]'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "project[]":
            raise ValueError("kind must be 'project[]'")

        return v


class AttributeDefinitions(BaseModel):
    """
    Represents definition of a resource or project.
    """

    ids: list[UUID] = Field(..., description="The unique identifier for the attributes")
    kind: str = Field(
        ..., description="The kind of the schema, must be 'attribute_definition[]'"
    )

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "attribute_definition[]":
            raise ValueError("kind must be 'attribute_definition[]'")

        return v


class Context(BaseModel):
    """
    Represents context configuration automatically inserted by the system.
    Contains authentication and deployment information.
    """

    user_api_key: str = Field(
        ...,
        description='User\'s API key. Include as "Authorization": Bearer <key> in the header to authenticate as the current user.',
    )
    base_url: str = Field(
        ..., description="Tektome's deployment base url ex: https://domain.tld"
    )
    execution_id: UUID = Field(
        ..., description="Execution id used to obtain additional extraction context"
    )

    @field_validator("base_url")
    def validate_base_url(cls, v):
        if not v:
            raise ValueError("base_url cannot be empty")

        # Check if URL has a valid scheme (http or https)
        if not v.startswith("http://") and not v.startswith("https://"):
            raise ValueError("base_url must start with 'http://' or 'https://'")

        return v