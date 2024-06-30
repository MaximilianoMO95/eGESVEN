from typing import cast
from sqlalchemy.orm import Session

from app.crud.product import ProductCrud as crud_product
from app.crud.product import CategoryCrud as crud_category
from app.schemas.product import CategoryCreate, ProductCreate


def test_create_and_get_category(db: Session) -> None:
    category_data = CategoryCreate(code="CAT002", description="Another Test Category")

    category = crud_category.create_category(db, category_data)
    assert category is not None
    assert cast(str, category.code) == "CAT002"
    assert cast(str, category.description) == "Another Test Category"

    fetched_category = crud_category.get_category(db, "CAT002")
    assert fetched_category is not None
    assert cast(str, fetched_category.code) == "CAT002"


def test_create_and_get_product(db: Session) -> None:
    product_data = ProductCreate(
        code="PROD002",
        description="Another Test Product",
        price=200,
        stock=20,
        category_code="CAT002"
    )

    product = crud_product.create_product(db, product_data)
    assert product is not None
    assert cast(str, product.code) == "PROD002"
    assert cast(str, product.description) == "Another Test Product"
    assert cast(int, product.price) == 200
    assert cast(int, product.stock) == 20

    fetched_product = crud_product.get_product(db, cast(int, product.id))
    assert fetched_product is not None
    assert cast(str, fetched_product.code) == "PROD002"
