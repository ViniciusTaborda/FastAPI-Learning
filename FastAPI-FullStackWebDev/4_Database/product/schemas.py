from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    """
    Model representing a single product
    """

    name: str
    description: str
    price: int


class Seller(BaseModel):
    """
    Model representing a single product
    """

    username: str
    email: str
    password: str


class DisplaySeller(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class DisplayProduct(BaseModel):
    name: str
    description: str
    seller: DisplaySeller

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
