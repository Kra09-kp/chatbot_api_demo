from fastapi import APIRouter
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from app import OPENAI_API_KEY, GROQ_API_KEY, use_openai

router = APIRouter(
    prefix="/templates",
    tags=["templates"],
    dependencies=[],
    responses={404: {"description": "Not found"}},

)


@router.get("/{query}")
async def generate(query:str):
    model =  ( ChatOpenAI(model="gpt-4o-mini",api_key=OPENAI_API_KEY) 
    if use_openai
    else ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)
    )
    messages = [
            SystemMessage(content="You are an assistant to generate templates for bussiness based on their requirements\
                Your response should be concise and small (around 25 to 30 words)."),
        ]

    response = model.invoke(messages)
    print(response.content)
    return {"response":response.content}