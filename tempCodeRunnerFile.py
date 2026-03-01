#                                                              Phase3-Setup Frontend

#Step1: Setup UI with streamlit (model provider, model, system prompt, web search, query)

import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-40-mini"]

provider=st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox ("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox ("Select OpenAI Model:", MODEL_NAMES_OPENAI)
#Step2: Connect with backend via URL

#step 2. Connect with backend via URL