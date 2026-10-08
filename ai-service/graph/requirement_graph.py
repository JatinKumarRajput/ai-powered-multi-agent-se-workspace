from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.requirement_agent import RequirementAnalysisAgent
from models.requirement_models import RequirementAnalysis


class RequirementState(TypedDict):
    requirements: str
    analysis: RequirementAnalysis | None


requirement_agent = RequirementAnalysisAgent()


def analyze_requirements(state: RequirementState):
    """Run the Requirement Analysis Agent."""

    result = requirement_agent.analyze(
        state["requirements"]
    )

    return {
        "analysis": result
    }


def build_requirement_graph():
    """Build and compile the Requirement Analysis workflow."""

    workflow = StateGraph(RequirementState)

    workflow.add_node(
        "requirement_analysis",
        analyze_requirements
    )

    workflow.add_edge(
        START,
        "requirement_analysis"
    )

    workflow.add_edge(
        "requirement_analysis",
        END
    )

    # IMPORTANT: compile the graph before returning it
    compiled_graph = workflow.compile()

    return compiled_graph