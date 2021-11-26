from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Product(BaseModel):
    name: str
    price: float
    discount: float
    discounted_price: float


class User(BaseModel):
    name: str
    email: str
