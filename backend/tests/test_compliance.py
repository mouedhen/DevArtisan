from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_create_compliance_check():
    response = client.post("/compliance", json={"name": "Test Compliance", "status": "Pending"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Compliance"
    assert response.json()["status"] == "Pending"

def test_get_compliance_check():
    response = client.get("/compliance/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Compliance"
    assert response.json()["status"] == "Pending"