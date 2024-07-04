from fastapi.testclient import TestClient
from typing import cast
from sqlalchemy.orm import Session

from app.tests.utils.product import create_random_product, create_random_category
from app.tests.utils.basket import create_basket_and_item
from app.schemas.basket import BasketItemCreate


def test_create_basket(client: TestClient) -> None:
    basket_data = { "client_id": 1, "items": [] }

    response = client.post("/baskets/", json=basket_data)
    assert response.status_code == 200

    data = response.json()
    assert data["client_id"] == basket_data["client_id"]
    assert data["items"] == []


def test_read_basket(client: TestClient, db: Session) -> None:
    basket_id, _ = create_basket_and_item(db)

    response = client.get(f"/baskets/{basket_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == basket_id


def test_add_item_to_basket(client: TestClient, db: Session) -> None:
    basket_id, _ = create_basket_and_item(db)

    create_random_category(db)
    product = create_random_product(db)

    item_data = BasketItemCreate(
            product_id=cast(int, product.id),
            quantity=2,
            price=cast(int, product.price)
    )
    response = client.post(f"/baskets/{basket_id}/items/", json=item_data.model_dump())
    assert response.status_code == 200

    data = response.json()
    assert data["product_id"] == item_data.product_id
    assert data["quantity"] == item_data.quantity
    assert data["price"] == item_data.price


def test_remove_item_from_basket(client: TestClient, db: Session) -> None:
    basket_id, item_id = create_basket_and_item(db)

    response = client.delete(f"/baskets/{basket_id}/items/{item_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == item_id


def test_get_basket_items(client: TestClient, db: Session) -> None:
    basket_id, _ = create_basket_and_item(db)

    response = client.get(f"/baskets/{basket_id}/items/")
    assert response.status_code == 200

    items = response.json()
    assert len(items) > 0
