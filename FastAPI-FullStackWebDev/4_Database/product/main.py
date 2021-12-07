from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import models, schemas
from database import engine, get_db
from passlib.context import CryptContext
from routers import product

app = FastAPI(
    title="Products API",
    description="Get details of all the products and seller in the website. \n Made by: Vinicius Taborda.",
    terms_of_service="https://github.com/ViniciusTaborda/FastAPI-Learning",
    contact={
        "Developer name": "Vinicius Taborda",
        "website": "https://www.linkedin.com/in/viniciustaborda/",
        "email": "vinicius.taborda.costa@gmail.com",
    },
    docs_url="/api_docs",
)

app.include_router(product.router)

models.base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post(
    "/seller",
    response_model=schemas.DisplaySeller,
    status_code=status.HTTP_201_CREATED,
    tags={"Seller"},
)
def add_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username, email=request.email, password=hashed_password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
