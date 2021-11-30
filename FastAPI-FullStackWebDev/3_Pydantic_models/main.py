from fastapi import FastAPI
from models import Profile, Product, User, Offer

app = FastAPI()


@app.post("/add/user/")
def add_user(profile: Profile):

    return {"name": profile.name, "email": profile.email, "age": profile.age}


@app.post("/add/offer/")
def add_offer(offer: Offer):

    return {offer}


@app.post("/add/product/{product_id}")
def add_user(product: Product, product_id: int, product_category: str):
    product.discounted_price = product.price - (product.price * product.discount) / 100

    return {
        "product_id": product_id,
        "product_category": product_category,
        "product": product,
    }


@app.post("/purchase")
def purchase(product: Product, user: User):

    return {
        "product": product,
        "user": user,
    }
