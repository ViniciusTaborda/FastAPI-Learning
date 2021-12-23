import random
import string

from schemas.users import UserCreate
from sqlalchemy.orm import Session
from db.repository.users import create_new_user


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_owner(db: Session):
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    password = random_lower_string()
    username = random_lower_string()
    user_schema = UserCreate(
        email=email,
        password=password,
        username=username,
    )
    user = create_new_user(user=user_schema, db=db)
    return user
