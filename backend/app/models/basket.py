from sqlalchemy import Integer
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Basket(Base):
    __tablename__ = "baskets"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))

    # Relationships
    client = relationship("Client", back_populates="basket")
    items = relationship("BasketItem", back_populates="basket", cascade="all, delete-orphan")


class BasketItem(Base):
    __tablename__ = "basket_items"
    id = Column(Integer, primary_key=True, index=True)
    basket_id = Column(Integer, ForeignKey("baskets.id"))
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    price = Column(Integer, nullable=False)

    # Relationships
    basket = relationship("Basket", back_populates="items")
    product = relationship("Product", back_populates="basket_items")
