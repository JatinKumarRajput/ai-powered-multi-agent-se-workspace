from langchain_google_genai import ChatGoogleGenerativeAI

from config import GOOGLE_API_KEY
from models.requirement_models import RequirementAnalysis


class RequirementAnalysisAgent:
    """
    Agent responsible for analyzing raw software requirements
    and converting them into a structured SDLC artifact.
    """

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash-lite",
            google_api_key=GOOGLE_API_KEY,
            temperature=0,
        )

        self.structured_llm = self.llm.with_structured_output(
            RequirementAnalysis
        )

    def analyze(self, requirements: str) -> RequirementAnalysis:

        prompt = f"""
You are a Requirement Analysis Agent in an AI-powered
Software Engineering Workspace.

Analyze the following software requirements and produce
a complete structured requirements artifact.

IMPORTANT:
You MUST populate every field in the required output schema.

For functional_requirements, explicitly extract every
user-facing or system capability described in the input.

Examples:
- User registration
- User login
- Product search
- Viewing product details
- Adding products to cart
- Placing orders

--- BEGIN REQUIREMENTS ---
{requirements}
--- END REQUIREMENTS ---

Follow these rules:

1. Identify all relevant actors.
2. Extract EVERY functional requirement explicitly supported
   by the input.
3. Extract non-functional requirements.
4. Identify ambiguous or incomplete requirements.
5. State reasonable assumptions when necessary.
6. Create testable acceptance criteria.
7. Do not invent major features that are not supported
   by the input.
8. Every field in the output schema must be populated.
9. Keep the analysis clear and suitable for downstream
   Architecture and Testing Agents.
"""

        result = self.structured_llm.invoke(prompt)

        return result