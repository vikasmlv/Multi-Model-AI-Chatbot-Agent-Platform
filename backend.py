#                                                        Phase2-Setup Backend (With FastAPI)
#step 1. Setup Pydantic Model (Schema Validation
from pydantic import BaseModel
from typing import List

from ai_agent import get_response_from_ai_agent


class RequestState(BaseModel):
    model_name : str
    model_provider : str
    system_prompt : str
    messages: List[str]
    allow_search: bool


#step 2. Setup Al Agent from FrontEnd Request
from fastapi import FastAPI

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title= "Langchain AI Agent ")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using LangGraph and Search tools
    It dynamically selects the model specifide in the requests
    
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error" : "Invalid model name. Kindly provide a valid Ai Model"}
    

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it!

    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response
    

#step 3. Run app & Explore Swagger UI Docs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1" , port=9999)