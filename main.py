from fastapi import FastAPI
from agentes.agente_basico import (
    graph,
    graph2,
    graph3
    )
from langchain_core.messages import HumanMessage
from .schemas.shema import AgenteBasico



app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}



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


@app.post("/agente-basico-3")
async def agente_basico_3(propmt:AgenteBasico):

    user_input = [HumanMessage(content=propmt.prompt)]

    user_input = {"messages": user_input}

    config = {"configurable": {"thread_id": propmt.user_id}}

    response = graph3.invoke(user_input, config)
    messages = response["messages"][-1].content
    return {
        "response":messages,
    }

    


    