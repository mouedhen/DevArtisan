from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_http_exception_handler():
    response = client.get("/error")
    assert response.status_code == 404
    assert response.json() == {"message": "Resource not found"}

def test_generic_exception_handler():
    response = client.get("/non_existent")
    assert response.status_code == 500
    assert response.json() == {"message": "An unexpected error occurred"}