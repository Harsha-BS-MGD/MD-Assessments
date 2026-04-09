"""
LangChain OpenRouter Question Answer Script
------------------------------------------
- Takes user input
- Sends to LLM (OpenRouter)
- Parses and prints response
"""

import os
import getpass
from dotenv import load_dotenv

from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser


def load_api_key() -> None:
    """Load OpenRouter API key from environment or prompt user."""
    load_dotenv()

    if not os.getenv("OPENROUTER_API_KEY"):
        os.environ["OPENROUTER_API_KEY"] = getpass.getpass(
            prompt="Enter your OpenRouter API key: "
        )


def create_model() -> ChatOpenRouter:
    """Initialize and return the ChatOpenRouter model."""
    return ChatOpenRouter(
        model="google/gemma-4-26b-a4b-it",
        temperature=0.7,
        max_tokens=100,
        max_retries=2,
    )


def get_user_question() -> str:
    """Prompt user to enter a question."""
    print("\n🤖 Ask the model a question")
    return input("👉 Enter your question: ").strip()


def main() -> None:
    """Main execution function."""
    load_api_key()

    model = create_model()
    parser = StrOutputParser()

    question = get_user_question()

    if not question:
        print("⚠️ No question provided. Exiting.")
        return

    try:
        response = model.invoke(question)
        result = parser.parse(response)
        print("\n✅ Response:\n")
        print(result)

    except Exception as error:  # pylint: disable=broad-except
        print(f"\n❌ Error occurred: {error}")


if __name__ == "__main__":
    main()