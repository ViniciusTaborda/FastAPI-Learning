from typing import List
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import models, schemas
from database import engine, session_local

app = FastAPI()

models.base.metadata.create_all(engine)


def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()


@app.get("/product")
def list_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()

    return products


@app.get("/product/{id}")
def retrieve_product(response: Response, id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
        return

    return product


@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = (
        db.query(models.Product)
        .filter(models.Product.id == id)
        .delete(synchronize_session=False)
    )

    return product


@app.put("/product/{id}")
def update_product(request: schemas.Product, id: int, db: Session = Depends(get_db)):
    product = (
        db.query(models.Product).filter(models.Product.id == id).update(request.dict())
    )

    return product


@app.post("/product")
def add_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(request.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return request
