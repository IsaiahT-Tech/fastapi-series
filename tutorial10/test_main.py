# Tutorial 10
from fastapi import FastAPI
from fastapi.testclient import TestClient 

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Hello World"}

client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    asser response.json() == {"message": "Hello World"}