from pydantic import BaseModel
from decimal import Decimal

# Esquema Pydantic para la clase Product
class ProductBase(BaseModel):
    titulo: str
    precio_compra: Decimal
    descripcion: str = None
    categoria: str = None
    url_imagen: str = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    rating: "Rating" # Relación con la clase Rating

    class Config:
        orm_mode = True

# Esquema Pydantic para la clase Rating
class RatingBase(BaseModel):
    rate: Decimal
    count: int

class RatingCreate(RatingBase):
    pass

class RatingUpdate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    product: Product  # Relación con la clase Product

    class Config:
        orm_mode = True