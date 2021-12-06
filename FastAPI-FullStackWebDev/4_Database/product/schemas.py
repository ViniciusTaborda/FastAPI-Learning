from pydantic import BaseModel


class Product(BaseModel):
    """
    Model representing a single product
    """

    name: str
    description: str
    price: int


class DisplayProduct(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = False
