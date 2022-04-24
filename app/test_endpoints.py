from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_home():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "text/html" in resp.headers["content-type"]


def test_post_home():
    resp = client.post("/")
    assert resp.status_code == 200
