from rag.vector_store import ProjectVectorStore


def main():

    print("\n========================================")
    print("          RAG VECTOR STORE TEST")
    print("========================================")

    # Create vector store
    store = ProjectVectorStore()

    # Add project context
    store.add_context(
        """
        The software system should allow customers to create an account,
        log in securely, search for products, view product details,
        add products to a shopping cart, and place orders.
        """,
        metadata={
            "type": "requirement",
            "source": "project_requirements"
        }
    )

    store.add_context(
        """
        The system architecture consists of a React frontend,
        Spring Boot backend, Python AI service, LangGraph agent
        orchestration, MongoDB database, and Chroma vector store.
        """,
        metadata={
            "type": "architecture",
            "source": "architecture_design"
        }
    )

    store.add_context(
        """
        The system should maintain security and support many
        concurrent users. Requirements should be validated
        through appropriate testing and acceptance criteria.
        """,
        metadata={
            "type": "testing",
            "source": "testing_requirements"
        }
    )

    print("\nProject context added to Chroma.")

    # Query the vector store
    query = "What can customers do with products and orders?"

    print("\nQUERY:")
    print(query)

    results = store.search(query, k=2)

    print("\nRETRIEVED CONTEXT:")

    for i, document in enumerate(results, start=1):

        print(f"\n--- Result {i} ---")

        print("Content:")
        print(document.page_content)

        print("\nMetadata:")
        print(document.metadata)

    print("\n========================================")
    print("             RAG TEST COMPLETE")
    print("========================================\n")


if __name__ == "__main__":
    main()