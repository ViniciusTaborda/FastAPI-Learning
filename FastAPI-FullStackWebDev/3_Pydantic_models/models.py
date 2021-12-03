from datetime import date
from typing import Set, List
from pydantic import BaseModel, Field, HttpUrl

from uuid import UUID


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Image(BaseModel):
    url: HttpUrl
    name: str


class Event(BaseModel):
    event_id: UUID
    start_date: date


class Product(BaseModel):
    name: str = Field(example="Example name")
    price: float = Field(
        title="Price of the item",
        description="Price of the item added into the system",
        gt=0,
    )
    discount: float
    discounted_price: float
    tags: Set[str] = Field(example={"eletronic", "cpu"})
    images: List[Image]

    class Config:
        schema_extra = {
            "name": "Phone",
            "price": 100,
            "discount": 0,
            "discounted_price": 0,
            "tags": ["Eletronics", "Computers"],
            "images": [
                {"url": "http://www.test_url.com" "name" "Phone image"},
                {"url": "http://www.test_url.com" "name" "Phone image side view"},
            ],
        }


class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Image]


class User(BaseModel):
    name: str
    email: str
