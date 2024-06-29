from sqlalchemy.types import Integer, SmallInteger, String
from sqlalchemy.schema import CheckConstraint, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Category(Base):
    __tablename__ = "categories"

    code = Column(String(30), primary_key=True)
    description = Column(String(300))

    # Relationships
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    code = Column(String(30), unique=True, index=True, nullable=False)
    description = Column(String(600), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(SmallInteger, nullable=False)
    category_code = Column(String(10), ForeignKey("categories.code"), nullable=False)

    # Relationships
    category = relationship("Category", back_populates="products")

    __table_args__ = (
        CheckConstraint("price >= 0", name="check_price_positive"),
        CheckConstraint("stock >= 0", name="check_stock_positive"),
    )
