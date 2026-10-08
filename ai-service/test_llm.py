from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY


def main():
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0
    )

    response = llm.invoke(
        "Explain what a software requirement is in one simple sentence."
    )

    print("\n===== GEMINI RESPONSE =====")
    print(response.content)
    print("===========================\n")


if __name__ == "__main__":
    main()