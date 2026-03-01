#                                                  ##Phase1-Create Al Agent##

import os


# 1. Setup API Keys for Groq , open Ai and Tavily
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from dotenv import load_dotenv
load_dotenv()

# 2. Setup LLM & Tools
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages import AIMessage

# LLM
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
openai_llm = ChatOpenAI(model="gpt-4o-mini")


system_prompt = "Act as an AI agent who is friendly and helpful."

def get_response_from_ai_agent(llm_id , query , allow_search , system_prompt , provider):
    if provider=="Groq":
        llm = ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm = ChatOpenAI(model=llm_id)

    # Tool
    tools =[ TavilySearch(max_results=2)] if allow_search else []
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    query = "Tell me about trends in the stock market"

    response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )

    messages = response.get("messages")

    ai_messages = [
        message.content
        for message in messages
        if isinstance(message, AIMessage)
    ]

    return ai_messages[-1]