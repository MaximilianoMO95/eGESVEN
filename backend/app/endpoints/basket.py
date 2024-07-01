from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.basket import Basket, BasketItem
from app.schemas.basket import BasketCreate, BasketItemCreate
import app.crud.basket as crud

from .deps import get_db


router = APIRouter()


@router.post("/baskets/", response_model=Basket)
def create_basket(basket: BasketCreate, db: Session = Depends(get_db)):
    return crud.create_basket(db=db, basket=basket)


@router.get("/baskets/{basket_id}", response_model=Basket)
def read_basket(basket_id: int, db: Session = Depends(get_db)):
    db_basket = crud.get_basket(db=db, basket_id=basket_id)
    if db_basket is None:
        raise HTTPException(status_code=404, detail="Basket not found")
    return db_basket


@router.post("/baskets/{basket_id}/items/", response_model=BasketItem)
def add_item_to_basket(basket_id: int, item: BasketItemCreate, db: Session = Depends(get_db)):
    return crud.add_item_to_basket(db=db, basket_id=basket_id, item=item)


@router.delete("/baskets/{basket_id}/items/{item_id}", response_model=BasketItem)
def remove_item_from_basket(basket_id: int, item_id: int, db: Session = Depends(get_db)):
    db_item = crud.remove_item_from_basket(db=db, basket_id=basket_id, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/baskets/{basket_id}/items/", response_model=List[BasketItem])
def get_basket_items(basket_id: int, db: Session = Depends(get_db)):
    return crud.get_basket_items(db=db, basket_id=basket_id)
