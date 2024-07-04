from sqlalchemy.orm import Session

from app.models.user import Client
from app.schemas.user import ClientCreate


def create(db: Session, client: ClientCreate) -> Client:
    db_client = Client(**client.model_dump())

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client


def get(db: Session, user_id: int) -> Client|None:
    return db.query(Client).filter(Client.user_id == user_id).first()
