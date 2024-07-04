from typing import List
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


def get(db: Session, product_id: int) -> Product|None:
    return db.query(Product).filter(Product.id == product_id).first()


def get_by_code(db: Session, code: str) -> Product|None:
    return db.query(Product).filter(Product.code == code).first()


def get_list(db: Session, skip: int = 0, limit: int = 10) -> List[Product]|None:
    return db.query(Product).offset(skip).limit(limit).all()


def create(db: Session, product: ProductCreate):
    db_product = Product(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def delete(db: Session, product_id: int) -> Product|None:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()

        return db_product


def update(db: Session, product_id: int, product_update: ProductCreate) -> Product|None:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        update_data = product_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)

        db.commit()
        db.refresh(db_product)

        return db_product
