from fastapi import FastAPI
from api.v1.Pais import router as pais_router
from api.v1.Depto import router as depto_router
from api.v1.Ciudad import router as ciudad_router

app = FastAPI(
    title="Api InRoute",
    description="Api DAO para el Proyecto InRoute",
    version="1.0",
    docs_url="/docs",  # URL para acceder a Swagger UI
    redoc_url="/redoc",  # URL para acceder a Redoc
)

@app.get("/", include_in_schema=False)
def read_root():
    return {
        "message": "¡Bienvenido a la API de InRoute!",
        "description": "Esta es la API para gestionar los datos de la aplicación InRoute.",
        "routes": "Explora las rutas en /docs para más información sobre los endpoints de la API."
    }

# Registrar el enrutador de la API de PAIS
app.include_router(pais_router)
app.include_router(depto_router)
app.include_router(ciudad_router)

# Inicia el servidor con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)