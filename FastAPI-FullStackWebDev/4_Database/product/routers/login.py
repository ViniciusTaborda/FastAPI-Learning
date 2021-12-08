from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, status, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, oauth2
import database, schemas, models

SECRET_KEY = "0e964fae66d645f8ddf4766d67105ba661405b16255155f455c3a09e544670df"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def generate_token(data: dict):
    to_enconde = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_enconde.update({"exp": expire})
    encoded_jwt = jwt.encode(to_enconde, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    seller = (
        db.query(models.Seller)
        .filter(models.Seller.username == request.username)
        .first()
    )

    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user_not_found"
        )

    if not pwd_context.verify(request.password, seller.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="invalid_password"
        )

    # Gen JWT token
    access_token = generate_token(data={"sub": seller.username})

    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise ...
    except:
        ...
