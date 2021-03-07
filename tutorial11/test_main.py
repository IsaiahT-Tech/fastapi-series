from fastapi.testclient import TestClient      

from main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todo/",
    json = {
        "name": "string",
        "due_date": "string",
        "description": "string"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "string",
        "due_date": "string",
        "description": "string"
    }

def test_get_all_todo():
    data = {
        "name": "string",
        "due_date": "string",
        "description": "string"
    }
    response = client.get("/todo/")
    assert response.status_code == 200

def test_get_todo():
    data = {
        "name": "string",
        "due_date": "string",
        "description": "string"
    }
    response = client.get("/todo/0")
    assert response.status_code == 200
    assert response.json() == data

def test_update_todo():
    response = client.put("/todo/0",
    json = {
        "name": "string",
        "due_date": "string",
        "description": "string"
    })
    assert response.status_code == 200
    assert response.json() ==  {
        "name": "string",
        "due_date": "string",
        "description": "string"
    }

def test_delete_todo():
    response = client.delete("/todo/0")
    assert response.status_code == 200
    assert response.json() ==  {
        "name": "string",
        "due_date": "string",
        "description": "string"
    }