from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

def test_create_todo():
    response = client.post('/create/')
    assert response.status_code == 200
    
