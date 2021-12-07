from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///../product.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base = declarative_base()


def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()
