from fastapi import FastAPI
import models
from database import engine
from routers import product, seller

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
app.include_router(seller.router)

models.base.metadata.create_all(engine)
