from typing import List
from sqlalchemy.orm import Session

from app.models.basket import Basket, BasketItem
from app.schemas.basket import BasketCreate, BasketItemCreate


def create(db: Session, basket: BasketCreate) -> Basket | None:
    db_basket = Basket(**basket.model_dump())

    db.add(db_basket)
    db.commit()
    db.refresh(db_basket)

    for item in basket.items:
        db_item = BasketItem(**item.model_dump(), basket_id=db_basket.id)
        db.add(db_item)

    db.commit()
    return db_basket


def get(db: Session, basket_id: int) -> BasketItem | None:
    return db.query(Basket).filter(Basket.id == basket_id).first()


def push_item(db: Session, basket_id: int, item: BasketItemCreate) -> BasketItem | None:
    db_item = BasketItem(**item.model_dump(), basket_id=basket_id)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def pop_item(db: Session, basket_id: int, item_id: int) -> BasketItem | None:
    db_item = db.query(BasketItem).filter(BasketItem.id == item_id, BasketItem.basket_id == basket_id).first()
    if db_item is None:
        return None

    db.delete(db_item)
    db.commit()

    return db_item


def get_items(db: Session, basket_id: int) -> List[BasketItem] | None:
    return db.query(BasketItem).filter(BasketItem.basket_id == basket_id).all()
