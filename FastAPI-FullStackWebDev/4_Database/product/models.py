from itertools import product
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from starlette.routing import replace_params
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
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    seller = relationship("Seller", back_populates="products")


class Seller(base):
    """
    Model that later on will be mapped to the database
    """

    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    products = relationship("Product", back_populates="seller")
