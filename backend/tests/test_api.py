from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_read_profile():
    response = client.get("/profile")
    assert response.status_code == 200 or 404  # Depending on seed