from pydantic import BaseModel, Field
from typing import List


class RequirementAnalysis(BaseModel):
    """Structured output produced by the Requirement Analysis Agent."""

    project_summary: str = Field(
        description="A concise summary of the software project."
    )

    actors: List[str] = Field(
        default_factory=list,
        description="Users, systems, or external entities that interact with the system."
    )

    functional_requirements: List[str] = Field(
        default_factory=list,
        description="Specific functions or capabilities the system must provide."
    )

    non_functional_requirements: List[str] = Field(
        default_factory=list,
        description="Quality attributes and constraints such as performance, security, scalability, and reliability."
    )

    ambiguities: List[str] = Field(
        default_factory=list,
        description="Requirements that are unclear, incomplete, or require clarification."
    )

    assumptions: List[str] = Field(
        default_factory=list,
        description="Reasonable assumptions made while interpreting the requirements."
    )

    acceptance_criteria: List[str] = Field(
        default_factory=list,
        description="Conditions that can be used to determine whether the requirements have been successfully implemented."
    )