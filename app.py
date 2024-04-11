from fastapi import FastAPI
from api.v1.Pais import router as pais_router

app = FastAPI(
    title="Api InRoute",
    description="Api DAO para el Proyecto InRoute",
    version="1.0",
    docs_url="/docs",  # URL para acceder a Swagger UI
    redoc_url="/redoc",  # URL para acceder a Redoc
)

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a la API de InRoute!"}

# Aquí puedes incluir las importaciones y configuraciones necesarias para tu API
# por ejemplo, importar y registrar los routers de otros módulos como `pais_router`
# from v1.Pais import router as pais_router
# app.include_router(pais_router, prefix="/v1/pais")

# Registrar el enrutador de la API de PAIS
app.include_router(pais_router)

# Puedes agregar otras rutas aquí si es necesario

# Inicia el servidor con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)