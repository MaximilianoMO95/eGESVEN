import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session

from app.core.db import Base, engine
from app.models.product import Category
from app.core.settings import ENVIRONMENT
from app.tests.utils.product import create_random_product


if ENVIRONMENT == "production":
    print("[ERROR] Cannot run script in production environment.")
    sys.exit(1)

Base.metadata.create_all(bind=engine)


categories = [
    {"code": "ALC", "description": "Alcoholic Beverages"},
    {"code": "WINE", "description": "Wines"},
    {"code": "BEER", "description": "Beers"},
    {"code": "SPIRITS", "description": "Spirits"},
]


def generate_fake_products(session: Session, num_products: int = 50):
    for category_data in categories:
        category = Category(**category_data)
        session.add(category)

    session.commit()

    for _ in range(num_products):
        create_random_product(session)


def main():
    session = Session(bind=engine)
    generate_fake_products(session)
    session.close()


if __name__ == "__main__": main()
