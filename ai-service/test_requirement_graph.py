from graph.requirement_graph import build_requirement_graph

def main():
    requirements = """
    We need an e-commerce website where customers can:

    1. Create an account.
    2. Log in securely.
    3. Search for products.
    4. View product details.
    5. Add products to a shopping cart.
    6. Place orders.

    The system should be secure and should support
    many concurrent users."""

     # Build LangGraph workflow
    graph = build_requirement_graph()

    # Initial state
    initial_state = {
        "requirements": requirements,
        "analysis": None
    }

    # Execute workflow
    final_state = graph.invoke(initial_state)

    analysis = final_state["analysis"]

    print("\n========================================")
    print("   LANGGRAPH REQUIREMENT WORKFLOW")
    print("========================================")

    print("\nPROJECT SUMMARY:")
    print(analysis.project_summary)

    print("\nACTORS:")
    for item in analysis.actors:
        print("-", item)

    print("\nFUNCTIONAL REQUIREMENTS:")
    for item in analysis.functional_requirements:
        print("-", item)

    print("\nNON-FUNCTIONAL REQUIREMENTS:")
    for item in analysis.non_functional_requirements:
        print("-", item)

    print("\nAMBIGUITIES:")
    for item in analysis.ambiguities:
        print("-", item)

    print("\nASSUMPTIONS:")
    for item in analysis.assumptions:
        print("-", item)

    print("\nACCEPTANCE CRITERIA:")
    for item in analysis.acceptance_criteria:
        print("-", item)

    print("\n========================================")
    print("       WORKFLOW COMPLETED")
    print("========================================\n")


if __name__ == "__main__":
    main()