from pydantic import BaseModel


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
