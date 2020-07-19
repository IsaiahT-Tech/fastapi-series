from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'Hello' : 'World'}

