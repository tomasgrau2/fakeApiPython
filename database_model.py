from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    precio = Column(float)
    categoria = Column(String)
    description = Column(String)
    url_imagen = Column(String)
    

class Rating(Base):
    __tablename__ = "rating"