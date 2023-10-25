from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from . import models, schemas



def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return (db.query(models.Product).filter(models.Product.id == product_id).options(joinedload(models.Product.rating).load_only(models.Rating.rate,models.Rating.count)).first())

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product_by_titulo(db: Session, titulo: int):
    return db.query(models.Product).filter(models.Product.titulo == titulo).first()


def delete_product_by_id(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    # Si se encontró el producto, elimínalo
    if product:
        db.delete(product)
        db.commit()
        return True  # Indica que se eliminó con éxito
    else:
        return False

def get_products_greater_than(db: Session, min_price: float):
    return db.query(models.Product).filter(models.Product.precio_compra > min_price).all()

def get_products_between_than(db: Session, min_price: float, max_price: float):
    return db.query(models.Product).filter((models.Product.precio_compra >= min_price) & (models.Product.precio_compra <= max_price)).all()

# def update_product(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
