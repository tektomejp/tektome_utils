"""Schema classes for Tektome resources and projects."""

from uuid import UUID

from pydantic import BaseModel, Field, field_validator


class Resource(BaseModel):
    """
    Represents a single resource.
    """

    id: UUID = Field(..., description="The unique identifier for the resource")
    kind: str = Field(..., description="The kind of the schema ,must be 'resource")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "resource":
            raise ValueError("kind must be 'resource'")

        return v


class Resources(BaseModel):
    """
    Represents a single resource.
    """

    id: list[UUID] = Field(..., description="The unique identifier for the resource")
    kind: str = Field(..., description="The kind of the schema ,must be 'resource[]")

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
    kind: str = Field(..., description="The kind of the schema ,must be 'project'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "project":
            raise ValueError("kind must be 'project'")

        return v


class Projects(BaseModel):
    """
    Represents a single project.
    """

    id: list[UUID] = Field(..., description="The unique identifier for the project")
    kind: str = Field(..., description="The kind of the schema ,must be 'project[]'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "project[]":
            raise ValueError("kind must be 'project[]'")

        return v


class AttributeDefinitions(BaseModel):
    """
    Represents definition of a resource or project.
    """

    id: list[UUID] = Field(..., description="The unique identifier for the attributes")
    kind: str = Field(
        ..., description="The kind of the schema ,must be 'attribute_definition[]'"
    )

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "attribute_definition[]":
            raise ValueError("kind must be 'attribute_definition[]'")

        return v
