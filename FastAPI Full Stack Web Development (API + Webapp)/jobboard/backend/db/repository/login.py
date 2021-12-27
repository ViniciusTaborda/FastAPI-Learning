from sqlalchemy.orm import Session
from db.models.users import User


def get_user(username: str, db: Session):
    return db.query(User).filter(User.email == username).first()
