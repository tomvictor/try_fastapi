from fastapi.testclient import TestClient

from app.core.config import settings


def test_create_item(client: TestClient) -> None:
    data = {"title": "hello", "description": "world"}
    response = client.get(f"{settings.API_V1_STR}")
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
