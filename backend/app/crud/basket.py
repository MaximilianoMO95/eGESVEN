from sqlalchemy.orm import Session
from app.models.basket import Basket, BasketItem
from app.schemas.basket import BasketCreate, BasketItemCreate


def create_basket(db: Session, basket: BasketCreate):
    db_basket = Basket(user_id=basket.user_id)
    db.add(db_basket)
    db.commit()
    db.refresh(db_basket)

    for item in basket.items:
        db_item = BasketItem(**item.model_dump(), basket_id=db_basket.id)
        db.add(db_item)

    db.commit()
    return db_basket


def get_basket(db: Session, basket_id: int):
    return db.query(Basket).filter(Basket.id == basket_id).first()


def add_item_to_basket(db: Session, basket_id: int, item: BasketItemCreate):
    db_item = BasketItem(**item.model_dump(), basket_id=basket_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def remove_item_from_basket(db: Session, basket_id: int, item_id: int):
    db_item = db.query(BasketItem).filter(BasketItem.id == item_id, BasketItem.basket_id == basket_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return db_item
    return None


def get_basket_items(db: Session, basket_id: int):
    return db.query(BasketItem).filter(BasketItem.basket_id == basket_id).all()
