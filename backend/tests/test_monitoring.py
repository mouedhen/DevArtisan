from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_create_monitoring_data():
    response = client.post("/monitoring", json={"metric": "CPU Usage", "value": "75%"})
    assert response.status_code == 200
    assert response.json()["metric"] == "CPU Usage"
    assert response.json()["value"] == "75%"

def test_get_monitoring_data():
    response = client.get("/monitoring/1")
    assert response.status_code == 200
    assert response.json()["metric"] == "CPU Usage"
    assert response.json()["value"] == "75%"