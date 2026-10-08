from agents.requirement_agent import RequirementAnalysisAgent

def main():
    requirements = """
    We need an e-commerce website where customers can create
    accounts, log in, search for products, view product details,
    add products to a shopping cart, and place orders.

    The system should be secure and should support many users."""

    agent = RequirementAnalysisAgent()

    result = agent.analyze(requirements)

    print("\n===== RAW RESULT =====")
    print(result)
    print("\n===== RESULT TYPE =====")
    print(type(result))
    print("======================\n")
    
    print("\n========== REQUIREMENT ANALYSIS ==========\n")

if __name__ == "__main__":
    main()