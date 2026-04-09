"""
LangChain SEO Blog Generator (OpenRouter)
----------------------------------------
- Step 1: Topic → Keywords
- Step 2: Keywords → Blog Outline
- Step 3: Outline → Full Article
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
        max_tokens=50,
        max_retries=2,
    )


def get_user_input() -> str:
    """Get topic input from user."""
    print("\n🚀 SEO Blog Generator\n")
    topic = input("👉 Enter topic: ").strip()
    return topic


def build_chains(model: ChatOpenRouter):
    """Create keyword, outline, and article chains."""

    # Step 1: Keywords
    prompt_keywords = ChatPromptTemplate.from_template(
        "Generate SEO keywords for the topic: {topic}"
    )
    keyword_chain = prompt_keywords | model | StrOutputParser()

    # Step 2: Outline
    prompt_outline = ChatPromptTemplate.from_template(
        "Create a structured blog outline using these keywords: {keywords}"
    )
    outline_chain = prompt_outline | model | StrOutputParser()

    # Step 3: Article
    prompt_article = ChatPromptTemplate.from_template(
        "Write a detailed blog article based on this outline: {outline}"
    )
    article_chain = prompt_article | model | StrOutputParser()

    return keyword_chain, outline_chain, article_chain


def main() -> None:
    """Main execution function."""
    load_api_key()

    model = create_model()
    keyword_chain, outline_chain, article_chain = build_chains(model)

    topic = get_user_input()

    if not topic:
        print("⚠️ Topic cannot be empty.")
        return

    try:
        # Step 1 → Keywords
        keywords = keyword_chain.invoke({"topic": topic})

        # Step 2 → Outline
        outline = outline_chain.invoke({"keywords": keywords})

        # Step 3 → Article
        article = article_chain.invoke({"outline": outline})

        print("\n🔑 Keywords:\n")
        print(keywords)

        print("\n🧩 Blog Outline:\n")
        print(outline)

        print("\n📄 Full Article:\n")
        print(article)

    except Exception as error:  # pylint: disable=broad-except
        print(f"\n❌ Error occurred: {error}")


if __name__ == "__main__":
    main()