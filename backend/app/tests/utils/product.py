from typing import Optional, cast
from sqlalchemy.orm import Session

from app.crud.product import ProductCrud as crud_product
from app.crud.product import CategoryCrud as crud_category
from app.models.product import Category, Product
from app.schemas.product import CategoryCreate, ProductCreate
from . import utils


def create_random_product(db: Session, category_code: Optional[str] = None) -> Product:
    if not category_code:
        category = create_random_category(db)
        category_code = cast(str, category.code)


    code = utils.random_code()
    description = utils.random_lower_str(len=200)
    price = utils.random_int(min=1, max=500000)
    stock = utils.random_int(min=0, max=100)

    product = ProductCreate(code=code, description=description, price=price, stock=stock, category_code=category_code)
    return crud_product.create_product(db, product)


def create_random_category(db: Session) -> Category:
    code = utils.random_code()
    description = utils.random_lower_str(len=200)

    category = CategoryCreate(code=code, description=description)
    return crud_category.create_category(db, category)
