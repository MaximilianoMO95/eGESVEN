from sqlalchemy import Integer
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Basket(Base):
    __tablename__ = "baskets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)

    # Relationships
    items = relationship("BasketItem", back_populates="basket")


class BasketItem(Base):
    __tablename__ = "basket_items"
    id = Column(Integer, primary_key=True, index=True)
    basket_id = Column(Integer, ForeignKey("baskets.id"))
    product_id = Column(Integer, index=True)
    quantity = Column(Integer, default=1, nullable=False)
    price = Column(Integer, nullable=False)

    # Relationships
    basket = relationship("Basket", back_populates="items")
