from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.tests.utils.product import create_random_category, create_random_product


def test_create_category(client: TestClient) -> None:
    category_data = { "code": "CAT001", "description": "Test Category" }

    response = client.post("/categories/", json=category_data)
    assert response.status_code == 200

    data = response.json()
    assert data["code"] == category_data["code"]
    assert data["description"] == category_data["description"]


def test_create_product(client: TestClient) -> None:
    product_data = {
        "code": "PROD001",
        "description": "Test Product",
        "name": "chicha de manzana",
        "price": 100,
        "stock": 10,
        "category_code": "CAT001"
    }

    response = client.post("/products/", json=product_data)
    assert response.status_code == 200

    data = response.json()
    for key, value in product_data.items():
        assert data[key] == value


def test_read_category(client: TestClient, db: Session) -> None:
    category = create_random_category(db);
    response = client.get(f"/categories/{category.code}")
    assert response.status_code == 200

    data = response.json()
    assert data["code"] == category.code
    assert data["description"] == category.description


def test_read_product(client: TestClient, db: Session) -> None:
    product = create_random_product(db);
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == product.id
    assert data["code"] == product.code
    assert data["name"] == product.name
    assert data["description"] == product.description
    assert data["price"] == product.price
    assert data["stock"] == product.stock
    assert data["category_code"] == product.category_code
