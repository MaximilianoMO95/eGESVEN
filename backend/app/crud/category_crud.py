from typing import List
from sqlalchemy.orm import Session

from app.models.product import Category
from app.schemas.product import CategoryCreate


def get(db: Session, code: str) -> Category|None:
    return db.query(Category).filter(Category.code == code).first()


def get_list(db: Session, skip: int = 0, limit: int = 10) -> List[Category]|None:
    return db.query(Category).offset(skip).limit(limit).all()


def create(db: Session, category: CategoryCreate) -> Category|None:
    db_category = Category(code=category.code, description=category.description)

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def delete(db: Session, code: str) -> Category|None:
    db_category = db.query(Category).filter(Category.code == code).first()
    if db_category:
        db.delete(db_category)
        db.commit()

        return db_category


def update(db: Session, code: str, category_update: CategoryCreate) -> Category|None:
    db_category = db.query(Category).filter(Category.code == code).first()
    if db_category:
        update_data = category_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_category, key, value)

        db.commit()
        db.refresh(db_category)

        return db_category
