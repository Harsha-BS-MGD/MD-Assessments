"""
LangChain 2-Step Blog Generator (OpenRouter)
-------------------------------------------
- Step 1: Generate blog title from topic
- Step 2: Generate blog content using title
- Uses OpenRouter + LCEL
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


def get_user_input() -> str:
    """Get topic input from user."""
    print("\n📝 Blog Generator\n")
    topic = input("👉 Enter topic: ").strip()
    return topic


def build_chains(model: ChatOpenRouter):
    """Create title and content chains using LCEL."""

    # Step 1: Title generation
    prompt_title = ChatPromptTemplate.from_template(
        "Generate a catchy blog title for the topic: {topic}"
    )
    title_chain = prompt_title | model | StrOutputParser()

    # Step 2: Content generation
    prompt_content = ChatPromptTemplate.from_template(
        "Write a short blog (3-5 lines) based on this title: {title}"
    )
    content_chain = prompt_content | model | StrOutputParser()

    return title_chain, content_chain


def main() -> None:
    """Main execution function."""
    load_api_key()

    model = create_model()
    title_chain, content_chain = build_chains(model)

    topic = get_user_input()

    if not topic:
        print("⚠️ Topic cannot be empty.")
        return

    try:
        # Step 1 → Generate Title
        title = title_chain.invoke({"topic": topic})

        # Step 2 → Generate Content using Title
        content = content_chain.invoke({"title": title})

        print("\n📝 Generated Blog Title:\n")
        print(title)

        print("\n📄 Blog Content:\n")
        print(content)

    except Exception as error:  # pylint: disable=broad-except
        print(f"\n❌ Error occurred: {error}")


if __name__ == "__main__":
    main()