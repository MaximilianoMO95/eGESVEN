from typing import cast
from sqlalchemy.orm import Session

from app.crud.product import ProductCrud as crud_product
from app.crud.product import CategoryCrud as crud_category
from app.schemas.product import CategoryCreate, ProductCreate


def test_create_and_get_category(db: Session) -> None:
    category_data = CategoryCreate(code="CAT002", description="Another Test Category")

    category = crud_category.create_category(db, category_data)
    assert category is not None
    assert cast(str, category.code) == cast(str, category_data.code)
    assert cast(str, category.description) == cast(str, category_data.description)

    fetched_category = crud_category.get_category(db, cast(str, category.code))
    assert fetched_category is not None
    assert cast(str, fetched_category.code) == cast(str, category.code)


def test_create_and_get_product(db: Session) -> None:
    product_data = ProductCreate(
        code="PROD002",
        name= "product 1",
        description="Another Test Product",
        price=200,
        stock=20,
        category_code="CAT002"
    )

    product = crud_product.create_product(db, product_data)
    assert product is not None
    assert cast(str, product.code) == cast(str, product_data.code)
    assert cast(str, product.name) == cast(str, product_data.name)
    assert cast(str, product.description) == cast(str, product_data.description)
    assert cast(int, product.price) == cast(int, product_data.price)
    assert cast(int, product.stock) == cast(int, product_data.stock)

    fetched_product = crud_product.get_product(db, cast(int, product.id))
    assert fetched_product is not None
    assert cast(str, fetched_product.code) == cast(str, product.code)
