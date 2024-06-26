from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float  
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index = True)
    name = Column(String, index = True)
    email = Column(String, unique = True, index = True)
    contactnumber = Column(Integer, index = True)

class Product(Base):
    _tablename_ = "products"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True)
    description = Column(String, index = True)  
    rating = Column(Float, index = True)
    price = Column(Float, index = True)