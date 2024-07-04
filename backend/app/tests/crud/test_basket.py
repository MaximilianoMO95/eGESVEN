from typing import cast
import pytest
from sqlalchemy.orm import Session

from app.schemas.basket import BasketCreate, BasketItemCreate
from app.crud import basket_crud

from app.tests.utils.product import create_random_product
from app.tests.utils.client import create_random_client


@pytest.fixture
def basket_data(db: Session) -> BasketCreate:
    client = create_random_client(db)

    return BasketCreate(client_id=cast(int, client.id), items=[])


@pytest.fixture
def basket_item_data(db: Session) -> BasketItemCreate:
    product = create_random_product(db)
    return BasketItemCreate(product_id=cast(int,product.id), quantity=1, price=cast(int, product.price))


def test_create_basket(db: Session, basket_data: BasketCreate) -> None:
    basket = basket_crud.create(db, basket_data)
    assert basket is not None
    assert cast(int, basket.client_id) == cast(int, basket_data.client_id)


def test_get_basket(db: Session, basket_data: BasketCreate) -> None:
    created_basket = basket_crud.create(db, basket_data)
    assert created_basket is not None

    fetched_basket = basket_crud.get(db, cast(int, created_basket.client_id))
    assert fetched_basket is not None
    assert cast(int, fetched_basket.client_id) == cast(int, created_basket.client_id)


def test_push_item(db: Session, basket_data: BasketCreate, basket_item_data: BasketItemCreate) -> None:
    basket = basket_crud.create(db, basket_data)
    assert basket is not None

    item = basket_crud.push_item(db, cast(int, basket.client_id), basket_item_data)
    assert item is not None
    assert cast(int, item.basket_id) == cast(int, basket.client_id)


def test_pop_item(db: Session, basket_data: BasketCreate, basket_item_data: BasketItemCreate) -> None:
    basket = basket_crud.create(db, basket_data)
    assert basket is not None

    item = basket_crud.push_item(db, cast(int, basket.client_id), basket_item_data)
    assert item is not None

    popped_item = basket_crud.pop_item(db, cast(int, basket.client_id), cast(int, item.id))
    assert popped_item is not None
    assert cast(int, popped_item.id) == cast(int, item.id)


def test_get_items(db: Session, basket_data: BasketCreate, basket_item_data: BasketItemCreate) -> None:
    basket = basket_crud.create(db, basket_data)
    assert basket is not None

    _ = basket_crud.push_item(db, cast(int, basket.client_id), basket_item_data)
    _ = basket_crud.push_item(db, cast(int, basket.client_id), basket_item_data)
    _ = basket_crud.push_item(db, cast(int, basket.client_id), basket_item_data)

    items = basket_crud.get_items(db, cast(int, basket.client_id))
    assert items is not None
    assert len(items) == 3
    assert cast(int, items[0].product_id) == cast(int, basket_item_data.product_id)
