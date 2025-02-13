from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"username": "testuser", "email": "testuser@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"

def test_login_for_access_token():
    response = client.post("/token", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"