from pydantic import BaseModel
from typing import List, Optional

from pydantic.config import ConfigDict

# Category Table
class CategoryBase(BaseModel):
    code: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    products: List["Product"] = []

    model_config = ConfigDict(from_attributes=True)


# Product Table
class ProductBase(BaseModel):
    code: str
    description: str
    price: int
    stock: int
    category_code: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
