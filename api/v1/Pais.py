from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any


from models.DataModel import Pais
from models.Pais import PaisBase
from config import SessionLocal
from abstract.AbstractAPI import AbstractAPI

# Crear un router para la API de Pais
router = APIRouter(prefix="/v1/pais", tags=["Pais"])

# Crear una instancia de AbstractAPI para Pais
pais_api = AbstractAPI(Pais, SessionLocal)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo país
@router.post("/", response_model=PaisBase)
def create_pais(pais: PaisBase, db: Session = Depends(get_db)):
    return pais_api.create(pais, db)

# Ruta para obtener un país por ID
@router.get("/{pais_id}", response_model=PaisBase)
def get_pais(pais_id: str, db: Session = Depends(get_db)):
    return pais_api.get(pais_id, db)

# Ruta para actualizar un país existente
@router.put("/{pais_id}", response_model=PaisBase)
def update_pais(pais_id: str, pais: PaisBase, db: Session = Depends(get_db)):
    return pais_api.update(pais_id, pais, db)

# Ruta para eliminar un país por ID
@router.delete("/{pais_id}", response_model=dict)
def delete_pais(pais_id: str, db: Session = Depends(get_db)):
    pais_api.delete(pais_id, db)
    return {"message": f"Pais with ID {pais_id} has been deleted"}

# Ruta para filtrar países por un campo y valor
@router.get("/filter/{field}/{value}", response_model=list[PaisBase])
def filter_paises(field: str, value: Any, db: Session = Depends(get_db)):
    return pais_api.filter(field, value, db)