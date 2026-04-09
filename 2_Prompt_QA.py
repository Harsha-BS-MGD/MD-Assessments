"""
LangChain Prompt Template with OpenRouter
----------------------------------------
- Takes role, topic, and audience from user
- Uses OpenRouter model
- Generates dynamic explanation
"""

import os
import getpass

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def load_api_key() -> None:
    """Load OpenRouter API key from .env or prompt user."""
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


def get_user_input() -> dict:
    """Collect role, topic, and audience from user."""
    print("\n🤖 Enter details below:\n")

    role = input("👉 Role: ").strip()
    topic = input("👉 Topic: ").strip()
    audience = input("👉 Audience: ").strip()

    return {
        "role": role,
        "topic": topic,
        "audience": audience,
    }


def build_chain(model: ChatOpenRouter):
    """Create LCEL chain using prompt template."""
    prompt = ChatPromptTemplate.from_template(
        "You are a {role}. Explain {topic} for {audience}."
    )

    parser = StrOutputParser()

    return prompt | model | parser


def main() -> None:
    """Main execution function."""
    load_api_key()

    model = create_model()
    chain = build_chain(model)

    user_input = get_user_input()

    if not all(user_input.values()):
        print("⚠️ All fields are required. Please try again.")
        return

    try:
        response = chain.invoke(user_input)

        print("\n✅ Response:\n")
        print(response)

    except Exception as error:  # pylint: disable=broad-except
        print(f"\n❌ Error occurred: {error}")


if __name__ == "__main__":
    main()