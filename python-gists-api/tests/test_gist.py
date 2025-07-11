import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_octocat_gists():
    response = client.get("/octocat")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():
        assert "id" in response.json()[0]
        assert "description" in response.json()[0]
        assert "url" in response.json()[0]
        assert "files" in response.json()[0]

def test_user_not_found():
    response = client.get("/thisuserdoesnotexistforsure")
    assert response.status_code == 404
    assert response.json()["detail"] == "GitHub user not found"