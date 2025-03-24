from fastapi import FastAPI
from pydantic import BaseModel
from agentes.agente_basico import (graph,graph2)
from langchain_core.messages import HumanMessage


app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}


class AgenteBasico(BaseModel):
    prompt: str

@app.post("/agente-basico")
async def agente_basico(prompt: AgenteBasico):


    
    inputs = [HumanMessage(content=prompt.prompt)]
    inputs = {"messages": inputs}
    response = graph.invoke(inputs)
    messages = response["messages"][-1].content
    return {
        "response":messages,
    }
    

@app.post("/agente-basico-2")
def agente_basico_2(prompt: AgenteBasico):


    user_input = [HumanMessage(content=prompt.prompt)]
    user_input = {"messages": user_input}
    response = graph2.invoke(user_input)

    messages = response["messages"][-1].content
    return {
        "response":messages,
    }


    pass