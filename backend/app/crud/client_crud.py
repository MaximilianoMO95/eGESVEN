from sqlalchemy.orm import Session

from app.models.user import Client
from app.schemas.user import ClientCreate


def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.model_dump())

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client
