from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.product import Category, Product
from app.schemas.product import CategoryCreate, ProductCreate
from app.crud.product import CategoryCrud as crud_category
from app.crud.product import ProductCrud as crud_product
from .deps import get_db


router = APIRouter()


@router.post("/categories/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud_category.get_category(db, code=category.code)
    if db_category:
        raise HTTPException(status_code=400, detail="Category with that code already exists")

    return crud_category.create_category(db, category)


@router.get("/categories/{code}", response_model=Category)
def read_category(code: str, db: Session = Depends(get_db)):
    category = crud_category.get_category(db, code)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.get("/categories/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_category.get_categories(db=db, skip=skip, limit=limit)


@router.post("/products/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product= crud_product.get_product_by_code(db, code=product.code)
    if db_product:
        raise HTTPException(status_code=400, detail="Product with that code already exists")

    return crud_product.create_product(db, product)


@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_product.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("/products/", response_model=list[Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_product.get_products(db=db, skip=skip, limit=limit)
