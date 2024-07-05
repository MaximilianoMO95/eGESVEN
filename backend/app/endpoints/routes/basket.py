from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.basket import BasketCreate, BasketItemCreate, BasketItemPublic, BasketPublic
from app.crud import basket_crud
from app.endpoints.deps import get_db


router = APIRouter()


@router.post("/baskets/", response_model=BasketPublic)
def create_basket(basket: BasketCreate, db: Session = Depends(get_db)):
    return basket_crud.create(db=db, basket=basket)


@router.get("/baskets/{basket_id}", response_model=BasketPublic)
def read_basket(basket_id: int, db: Session = Depends(get_db)):
    db_basket = basket_crud.get(db=db, basket_id=basket_id)
    if db_basket is None:
        raise HTTPException(status_code=404, detail="Basket not found")
    return db_basket


@router.post("/baskets/{basket_id}/items/", response_model=BasketItemPublic)
def add_item_to_basket(basket_id: int, item: BasketItemCreate, db: Session = Depends(get_db)):
    return basket_crud.push_item(db=db, basket_id=basket_id, item=item)


@router.delete("/baskets/{basket_id}/items/{item_id}", response_model=BasketItemPublic)
def remove_item_from_basket(basket_id: int, item_id: int, db: Session = Depends(get_db)):
    db_item = basket_crud.pop_item(db=db, basket_id=basket_id, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/baskets/{basket_id}/items/", response_model=List[BasketItemPublic])
def get_basket_items(basket_id: int, db: Session = Depends(get_db)):
    return basket_crud.get_items(db=db, basket_id=basket_id)
