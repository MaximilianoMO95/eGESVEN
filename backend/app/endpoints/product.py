from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.product import Product, ProductCreate
from app.crud import product_crud
from .deps import get_db


router = APIRouter()


@router.post("/products/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product= product_crud.get_by_code(db, code=product.code)
    if db_product:
        raise HTTPException(status_code=400, detail="Product with that code already exists")

    return product_crud.create(db, product)


@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = product_crud.get(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("/products/", response_model=list[Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return product_crud.get_list(db=db, skip=skip, limit=limit)
