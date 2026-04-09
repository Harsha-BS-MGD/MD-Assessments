import getpass
import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass.getpass("Enter your OpenRouter API key: ")




model = ChatOpenRouter(
    #model="anthropic/claude-sonnet-4.5"
    model = "google/gemma-4-26b-a4b-it",
    temperature=0,
    max_tokens=1024,
    max_retries=2,
    # other params...
)

print("Asking Model QUestiona please answer the following question")

question = input("What is Your Question")

parser = StrOutputParser()

reresponse = model.invoke(question,)
res = parser.parse(reresponse)

print(res)