from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models.Pais import Pais
from config import SessionLocal
from typing import List
from datetime import datetime


# Crear un enrutador con el prefijo "/v1/pais"
router = APIRouter(prefix="/v1/pais")

# Definir un modelo Pydantic para la tabla PAIS
class PaisBase(BaseModel):
    id: str
    nombre: str
    indicativo_telefonico: int
    estado: int = 1
    fecha_registro: datetime
    fecha_actualizacion: datetime
    usuario_id: str | None = None
    ip_address: str | None = None

    class Config:
        from_attributes = True

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Operación para crear un nuevo país
@router.post("/", response_model=PaisBase)
def create_pais(pais: PaisBase, db: Session = Depends(get_db)):
    db_pais = Pais(**pais.dict())
    db.add(db_pais)
    db.commit()
    db.refresh(db_pais)
    return db_pais

# Operación para leer un país por ID
@router.get("/{pais_id}", response_model=PaisBase)
def read_pais(pais_id: str, db: Session = Depends(get_db)):
    db_pais = db.query(Pais).filter(Pais.ID == pais_id).first()
    if db_pais is None:
        raise HTTPException(status_code=404, detail="País no encontrado")
    return db_pais

# Operación para leer todos los países (con paginación opcional)
@router.get("/", response_model=List[PaisBase])
def read_all_paises(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    paises = db.query(Pais).offset(skip).limit(limit).all()
    return paises

# Operación para actualizar un país por ID
@router.put("/{pais_id}", response_model=PaisBase)
def update_pais(pais_id: str, pais: PaisBase, db: Session = Depends(get_db)):
    db_pais = db.query(Pais).filter(Pais.ID == pais_id).first()
    if db_pais is None:
        raise HTTPException(status_code=404, detail="País no encontrado")
    # Actualizar los campos del país existente con los valores del modelo recibido
    for key, value in pais.dict().items():
        setattr(db_pais, key, value)
    db.commit()
    db.refresh(db_pais)
    return db_pais

# Operación para eliminar un país por ID
@router.delete("/{pais_id}")
def delete_pais(pais_id: str, db: Session = Depends(get_db)):
    db_pais = db.query(Pais).filter(Pais.ID == pais_id).first()
    if db_pais is None:
        raise HTTPException(status_code=404, detail="País no encontrado")
    db.delete(db_pais)
    db.commit()
    return {"detail": "País eliminado con éxito"}

# Operación para filtrar países por un campo y valor
@router.get("/filter/{field}/{value}")
def filter_paises(
    field: str,  # Argumento sin valor predeterminado
    value: str,  # Argumento sin valor predeterminado
    db: Session = Depends(get_db)  # Argumento con valor predeterminado (dependencia)
):
    # Componer la consulta según el campo y el valor
    if hasattr(Pais, field):
        paises = db.query(Pais).filter(getattr(Pais, field) == value).all()
        return paises
    else:
        raise HTTPException(status_code=400, detail="Campo de filtrado no válido")