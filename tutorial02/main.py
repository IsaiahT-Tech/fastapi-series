from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'Hello' : 'World'}

@app.get("/component/{component_id}") # path parameter
async def get_component(component_id: int):
    return {"component_id": component_id}

@app.get("/component/")
async def read_component(number: int, text: Optional[str] = None):  # query parameter
    return {"number": number, "text": text}


