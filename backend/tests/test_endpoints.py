"""
Integration tests for the API endpoints.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_project_plan():
    response = client.post("/project/plan", json={"title": "Test Project", "description": "Create a web application"})
    assert response.status_code == 200
    assert "project plan" in response.json()["plan"].lower()

def test_generate_code():
    # Create a new project
    response = client.post("/project/plan", json={"title": "Test Project", "description": "Create a web application"})
    assert response.status_code == 200
    project_id = response.json()["id"]

    # Generate code for the project
    response = client.post(f"/project/generate-code/{project_id}")
    assert response.status_code == 200
    assert "Code generated and saved successfully" in response.json()["message"]

def test_create_review():
    # Create a new project
    response = client.post("/project/plan", json={"title": "Test Project", "description": "Create a web application"})
    assert response.status_code == 200
    project_id = response.json()["id"]

    # Create a review for the project
    response = client.post("/review", json={"project_id": project_id, "reviewer": "John Doe", "comments": "Looks good!", "status": "approved"})
    assert response.status_code == 200
    assert response.json()["reviewer"] == "John Doe"
    assert response.json()["comments"] == "Looks good!"
    assert response.json()["status"] == "approved"

def test_create_security_issue():
    # Create a new project
    response = client.post("/project/plan", json={"title": "Test Project", "description": "Create a web application"})
    assert response.status_code == 200
    project_id = response.json()["id"]

    # Create a security issue for the project
    response = client.post("/security", json={"project_id": project_id, "title": "SQL Injection", "description": "SQL injection vulnerability found", "severity": "high"})
    assert response.status_code == 200
    assert response.json()["title"] == "SQL Injection"
    assert response.json()["description"] == "SQL injection vulnerability found"
    assert response.json()["severity"] == "high"

def test_create_deployment():
    # Create a new project
    response = client.post("/project/plan", json={"title": "Test Project", "description": "Create a web application"})
    assert response.status_code == 200
    project_id = response.json()["id"]

    # Create a deployment for the project
    response = client.post("/deploy", json={"project_id": project_id, "environment": "production"})
    assert response.status_code == 200
    assert response.json()["environment"] == "production"
    assert response.json()["status"] == "deployed"