from sqlalchemy.orm import Session
from schema.schema import Response
from models.models import Responses

def create_item(db: Session, item: Response):
    db_item = Responses(name=item.name, email=item.email, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def view(db: Session):
    return db.query(Responses).all()

