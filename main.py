from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/products/", response_model=list[schemas.ProductBase])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@app.get("/product/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="product not found")
    return db_product

@app.get("/products/{min_price}", response_model=list[schemas.ProductBase])
def read_products_greater_than(min_price: float, db: Session = Depends(get_db),):
    products = crud.get_products_greater_than(db, min_price)
    if not products:
        raise HTTPException(status_code=404, detail="No products found with a price greater than the specified value")
    return products

@app.get("/products_between/", response_model=list[schemas.ProductBase])
def read_products_between_than(min_price: float = Query(..., title="Precio mínimo"),max_price: float = Query(..., title="Precio máximo"),db: Session = Depends(get_db)):
    products = crud.get_products_between_than(db, min_price, max_price)
    
    if not products:
        raise HTTPException(status_code=404, detail="No products found within the specified price range")
    
    return products

@app.post("/products/")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    # Verifica si un producto con el mismo título ya existe
    existing_product = crud.get_product_by_titulo(db, titulo=product.titulo)
    if existing_product:
        raise HTTPException(status_code=400, detail="Product with the same title already exists")

    # Si no existe un producto con el mismo título, crea el nuevo producto
    return crud.create_product(db=db, product=product)



@app.delete("/products/{product_id}", response_model=bool)
def delete_product(product_id: int,db: Session = Depends(get_db)):
    # Intenta eliminar el producto utilizando la función delete_product_by_id
    deleted = crud.delete_product_by_id(db, product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")

    return True


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
