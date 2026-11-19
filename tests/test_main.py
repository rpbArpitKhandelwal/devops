from starlette.testclient import TestClient

from app.main import APP_NAME, app

client = TestClient(app)


def test_home() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "application": APP_NAME,
        "status": "success",
    }


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_orders() -> None:
    response = client.get("/orders")
    payload = response.json()

    assert response.status_code == 200
    assert isinstance(payload["orders"], list)
    assert len(payload["orders"]) == 2
    assert payload["orders"][0] == {"id": 1, "item": "Laptop", "status": "shipped"}
    assert payload["orders"][1] == {"id": 2, "item": "Keyboard", "status": "processing"}
    assert payload["timestamp"].endswith("+00:00")
