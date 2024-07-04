from typing import Optional, cast
from sqlalchemy.orm import Session
from sqlalchemy import delete

from app.crud import basket_crud
from app.models.basket import Basket
from app.models.user import Client
from app.schemas.basket import BasketCreate, BasketItemCreate
from app.tests.utils.client import create_random_client
from app.tests.utils.product import create_random_product


def create_basket_and_item(db: Session, client: Optional[Client] = None) -> tuple[int, int]:
    if client is None:
        client = create_random_client(db)


    product = create_random_product(db)
    item_data = BasketItemCreate(
            product_id = cast(int, product.id),
            quantity = 1,
            price = cast(int, product.price)
    )
    basket_data = BasketCreate(client_id=cast(int, client.id), items=[])

    basket = basket_crud.create(db, basket_data)
    assert basket is not None

    _ = basket_crud.push_item(db, cast(int, basket.id), item_data)
    assert len(basket.items) == 1

    basket_id = cast(int, basket.id)
    item_id = cast(int, basket.items[0].id)

    return (basket_id, item_id)


def empty_basket_records(db: Session) -> None:
    db.execute(delete(Basket))
    db.commit()
