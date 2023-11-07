Para utilizar esta API se deben instalar
- SQLAlchemy
- FastApi
- Uvicorn

Para levantar la API, posicionarse en el directorio anterior al de la API y ejecutar en bash el comando:
- uvicorn sql_app.main:app

Para interactuar con la API, en su navegador web ingrese la direccion proporcionada por la api, usualmente será http://127.0.0.1:8000, para ver la API se tiene que agregar a esta dirección la ruta docs, quedando la URL http://127.0.0.1:8000/docs
