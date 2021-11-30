from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Image(BaseModel):
    url: HttpUrl
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(
        title="Price of the item",
        description="Price of the item added into the system",
        gt=0,
    )
    discount: float
    discounted_price: float
    tags: Set[str]
    images: List[Image]

    class Config:
        schema_extra = {
            "name": "Phone",
            "price": 100,
            "discount": 0,
        }


class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Image]


class User(BaseModel):
    name: str
    email: str
