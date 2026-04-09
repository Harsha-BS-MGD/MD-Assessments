"""
Multi-Platform Blog Generator using LangChain + OpenRouter.

Generates blog-style content for:
- Twitter (thread format)
- LinkedIn (professional post)
- Instagram (caption/story style)

Input: Topic from user
"""

import os
import getpass
from dotenv import load_dotenv

from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def load_api_key() -> None:
    """Load OpenRouter API key from environment or prompt user."""
    load_dotenv()

    if not os.getenv("OPENROUTER_API_KEY"):
        os.environ["OPENROUTER_API_KEY"] = getpass.getpass(
            "Enter your OpenRouter API key: "
        )


def create_model() -> ChatOpenRouter:
    """Initialize and return the ChatOpenRouter model."""
    return ChatOpenRouter(
        model="google/gemma-4-26b-a4b-it",
        temperature=0.7,
        max_tokens=200,
        max_retries=2,
    )


def create_prompts():
    """Create blog-style prompts for each platform."""

    twitter_prompt = ChatPromptTemplate.from_template(
        "Create a Twitter thread (4-5 tweets) explaining the topic: {topic}"
    )

    linkedin_prompt = ChatPromptTemplate.from_template(
        "Write a professional LinkedIn blog-style post on: {topic}"
    )

    instagram_prompt = ChatPromptTemplate.from_template(
        "Write an engaging Instagram caption (story style with emojis and hashtags) about: {topic}"
    )

    return twitter_prompt, linkedin_prompt, instagram_prompt


def main() -> None:
    """Run the multi-platform blog generator."""

    # Load API key
    load_api_key()

    # Initialize model and parser
    model = create_model()
    parser = StrOutputParser()

    # User input
    topic = input("Enter blog topic: ").strip()

    if not topic:
        print("❌ Topic cannot be empty.")
        return

    # Create prompts
    twitter_prompt, linkedin_prompt, instagram_prompt = create_prompts()

    # Create chains
    twitter_chain = twitter_prompt | model | parser
    linkedin_chain = linkedin_prompt | model | parser
    instagram_chain = instagram_prompt | model | parser

    print("\n⏳ Generating blog content...\n")

    # Generate content
    twitter_blog = twitter_chain.invoke({"topic": topic})
    linkedin_blog = linkedin_chain.invoke({"topic": topic})
    instagram_blog = instagram_chain.invoke({"topic": topic})

    # Output
    print("🐦 Twitter Thread:\n", twitter_blog, "\n")
    print("💼 LinkedIn Blog:\n", linkedin_blog, "\n")
    print("📸 Instagram Blog:\n", instagram_blog, "\n")


if __name__ == "__main__":
    main()