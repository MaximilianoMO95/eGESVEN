from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.product import Category, CategoryCreate
from app.crud import category_crud
from .deps import get_db


router = APIRouter()


@router.post("/categories/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = category_crud.get(db, code=category.code)
    if db_category:
        raise HTTPException(status_code=400, detail="Category with that code already exists")

    return category_crud.create(db, category)


@router.get("/categories/{code}", response_model=Category)
def read_category(code: str, db: Session = Depends(get_db)):
    category = category_crud.get(db, code)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.get("/categories/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return category_crud.get_list(db=db, skip=skip, limit=limit)
