from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
print("tt")

def test_read_main():
    print("test")
    response = client.get("/")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"id": 1, "name": "test"}
