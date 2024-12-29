import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_prime_number():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

def test_non_prime_number():
    response = client.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_zero():
    response = client.get("/check_prime/0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_negative_number():
    response = client.get("/check_prime/-5")
    assert response.status_code == 200
    assert response.json() == {"number": -5, "is_prime": False}
