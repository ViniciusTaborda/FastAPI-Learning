from itertools import product
from sqlalchemy import Column, Integer, String
from database import base


class Product(base):
    """
    Model that later on will be mapped to the database
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(String)
