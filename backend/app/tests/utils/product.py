from typing import Optional, cast
from sqlalchemy.orm import Session

from app.crud import product_crud, category_crud
from app.models.product import Category, Product
from app.schemas.product import CategoryCreate, ProductCreate

from . import helpers


def create_random_product(db: Session, category_code: Optional[str] = None) -> Product:
    if not category_code:
        category = create_random_category(db)
        category_code = cast(str, category.code)


    code = helpers.random_code()
    name = helpers.random_lower_str(len=30)
    description = helpers.random_lower_str(len=200)
    price = helpers.random_int(min=1, max=500000)
    stock = helpers.random_int(min=0, max=100)

    product = ProductCreate(code=code, name=name, description=description, price=price, stock=stock, category_code=category_code)
    return product_crud.create(db, product)


def create_random_category(db: Session) -> Category:
    code = helpers.random_code()
    description = helpers.random_lower_str(len=200)

    category = CategoryCreate(code=code, description=description)
    return category_crud.create(db, category)
