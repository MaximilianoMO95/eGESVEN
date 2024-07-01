from typing import List
from sqlalchemy.orm import Session

from app.models.product import Category, Product
from app.schemas.product import CategoryCreate, ProductCreate


class CategoryCrud:

    @staticmethod
    def get_category(db: Session, code: str) -> Category|None:
        return db.query(Category).filter(Category.code == code).first()


    @staticmethod
    def get_categories(db: Session, skip: int = 0, limit: int = 10) -> List[Category]|None:
        return db.query(Category).offset(skip).limit(limit).all()


    @staticmethod
    def create_category(db: Session, category: CategoryCreate) -> Category|None:
        db_category = Category(code=category.code, description=category.description)

        db.add(db_category)
        db.commit()
        db.refresh(db_category)

        return db_category


    @staticmethod
    def delete_category(db: Session, code: str) -> Category|None:
        db_category = db.query(Category).filter(Category.code == code).first()
        if db_category:
            db.delete(db_category)
            db.commit()

            return db_category


    @staticmethod
    def update_category(db: Session, code: str, category_update: CategoryCreate) -> Category|None:
        db_category = db.query(Category).filter(Category.code == code).first()
        if db_category:
            update_data = category_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_category, key, value)

            db.commit()
            db.refresh(db_category)

            return db_category


class ProductCrud:

    @staticmethod
    def get_product(db: Session, product_id: int) -> Product|None:
        return db.query(Product).filter(Product.id == product_id).first()


    @staticmethod
    def get_product_by_code(db: Session, code: str) -> Product|None:
        return db.query(Product).filter(Product.code == code).first()


    @staticmethod
    def get_products(db: Session, skip: int = 0, limit: int = 10) -> List[Product]|None:
        return db.query(Product).offset(skip).limit(limit).all()


    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        db_product = Product(
            code=product.code,
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
            category_code=product.category_code,
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product


    @staticmethod
    def delete_product(db: Session, product_id: int) -> Product|None:
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            db.delete(db_product)
            db.commit()

            return db_product


    @staticmethod
    def update_product(db: Session, product_id: int, product_update: ProductCreate) -> Product|None:
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            update_data = product_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_product, key, value)

            db.commit()
            db.refresh(db_product)

            return db_product
