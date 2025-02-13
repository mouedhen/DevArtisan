"""
Security tests for the DevArtisan application.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import User
from sqlalchemy.orm import Session

client = TestClient(app)

def test_sql_injection():
    """
    Test for SQL injection vulnerability.
    """
    response = client.get("/user?id=1 OR 1=1")
    assert response.status_code == 400  # Expecting a bad request response

def test_xss():
    """
    Test for Cross-Site Scripting (XSS) vulnerability.
    """
    response = client.post("/project", json={"title": "<script>alert('XSS')</script>"})
    assert response.status_code == 400  # Expecting a bad request response

def test_csrf():
    """
    Test for Cross-Site Request Forgery (CSRF) vulnerability.
    """
    response = client.post("/auth/token", data={"username": "test", "password": "test"})
    assert response.status_code == 401  # Unauthorized since CSRF token is missing

def test_password_hashing(db: Session):
    """
    Test if passwords are hashed correctly.
    """
    user = db.query(User).filter(User.username == "testuser").first()
    assert user is not None
    assert user.hashed_password != "plaintextpassword"