from pydantic import BaseModel
from typing import List

from pydantic.config import ConfigDict


class BasketItemBase(BaseModel):
    product_id: int
    quantity: int
    price: int


class BasketItemCreate(BasketItemBase):
    pass


class BasketItem(BasketItemBase):
    id: int
    basket_id: int

    model_config = ConfigDict(from_attributes=True)


class BasketBase(BaseModel):
    client_id: int


class BasketCreate(BasketBase):
    items: List[BasketItemCreate] = []


class Basket(BasketBase):
    id: int
    items: List[BasketItem] = []

    model_config = ConfigDict(from_attributes=True)
