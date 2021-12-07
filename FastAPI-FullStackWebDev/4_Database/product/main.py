from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import models, schemas
from database import engine, session_local
from passlib.context import CryptContext

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

models.base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()


@app.get("/product", tags={"Products"})
def list_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()

    return products


@app.get("/product/{id}", tags={"Products"})
def retrieve_product(response: Response, id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
        return

    return product


@app.delete("/product/{id}", tags={"Products"})
def delete_product(id: int, db: Session = Depends(get_db)):
    product = (
        db.query(models.Product)
        .filter(models.Product.id == id)
        .delete(synchronize_session=False)
    )

    return product


@app.put("/product/{id}", tags={"Products"})
def update_product(request: schemas.Product, id: int, db: Session = Depends(get_db)):
    product = (
        db.query(models.Product).filter(models.Product.id == id).update(request.dict())
    )

    return product


@app.post(
    "/product",
    response_model=schemas.DisplayProduct,
    status_code=status.HTTP_201_CREATED,
    tags={"Products"},
)
def add_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name,
        description=request.description,
        price=request.price,
        seller_id=1,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


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
