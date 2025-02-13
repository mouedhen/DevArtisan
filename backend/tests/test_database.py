from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database import SessionLocal, engine
from backend.app import models

client = TestClient(app)

models.Base.metadata.create_all(bind=engine)

def test_create_item():
    response = client.post("/items/", json={"title": "Test Item", "description": "This is a test item"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Item"
    assert response.json()["description"] == "This is a test item"

def test_read_item():
    response = client.post("/items/", json={"title": "Test Item", "description": "This is a test item"})
    item_id = response.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Item"
    assert response.json()["description"] == "This is a test item"