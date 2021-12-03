from pydantic import BaseModel


class Product(BaseModel):
    """
    Model representing a single product
    """

    name: str
    description: str
    price: int
