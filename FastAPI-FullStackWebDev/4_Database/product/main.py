from fastapi import FastAPI
import models, schemas
from database import engine

app = FastAPI()

models.base.metadata.create_all(engine)

@app.post("/product")
def add_product(request: schemas.Product):
    return request
