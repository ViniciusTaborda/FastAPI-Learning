from fastapi import FastAPI

app = FastAPI()


@app.get("/user/admin")
def profile():
    return f"This is the admin page"


@app.get("/user/{username}")
def profile(username: str):
    return f"This is a profile page for {username}"


# Typed query params
@app.get("/products")
def products(id: int, price: float):
    return f"Product with id {id} and price {price}"


# Default values for query params
@app.get("/materials")
def materials(id: int = 0, price: float = 0.0):
    return f"Material with id {id} and price {price}"


# Query params and path params
@app.get("/companies/{number}")
def companies(number: int, id: int = 0, price: float = 0.0):
    return f"Companie with number {number}, id {id} and price {price}"


# Required path params
@app.get("/phones/{number}")
def phones(number: int, id: int = 0):
    return f"Phone with number {number}, id {id}"
