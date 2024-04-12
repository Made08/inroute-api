from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from models.DataModel import Ciudad
from models.Ciudad import CiudadBase
from config import SessionLocal
# Crear un enrutador con el prefijo "/v1/ciudad"
router = APIRouter(prefix="/v1/ciudad", tags=["Ciudad"])

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CiudadBase)
def create_ciudad(ciudad: CiudadBase, db: Session = Depends(get_db)):
    db_ciudad = Ciudad(**ciudad.model_dump())
    db.add(db_ciudad)
    db.commit()
    db.refresh(db_ciudad)
    return db_ciudad

@router.get("/{ciudad_id}", response_model=CiudadBase)
def read_ciudad(ciudad_id: str, db: Session = Depends(get_db)):
    db_ciudad = db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()
    if not db_ciudad:
        raise HTTPException(status_code=404, detail="Ciudad not found")
    return db_ciudad

@router.put("/{ciudad_id}", response_model=CiudadBase)
def update_ciudad(ciudad_id: str, ciudad: CiudadBase, db: Session = Depends(get_db)):
    db_ciudad = db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()
    if not db_ciudad:
        raise HTTPException(status_code=404, detail="Ciudad not found")
    for key, value in ciudad.model_dump().items():
        setattr(db_ciudad, key, value)
    db.commit()
    db.refresh(db_ciudad)
    return db_ciudad

@router.delete("/{ciudad_id}", response_model=CiudadBase)
def delete_ciudad(ciudad_id: str, db: Session = Depends(get_db)):
    db_ciudad = db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()
    if not db_ciudad:
        raise HTTPException(status_code=404, detail="Ciudad not found")
    db.delete(db_ciudad)
    db.commit()
    return db_ciudad

@router.get("/", response_model=List[CiudadBase])
def list_ciudades(db: Session = Depends(get_db)):
    return db.query(Ciudad).all()

@router.get("/filter/{field}/{value}", response_model=List[CiudadBase])
def filter_ciudades(
    field: str,  # Argumento sin valor predeterminado
    value: str,  # Argumento sin valor predeterminado
    db: Session = Depends(get_db)  # Argumento con valor predeterminado (dependencia)
):
    # Valida existencia del campo
    if not hasattr(Ciudad, field):
        raise HTTPException(status_code=400, detail="Campo de filtrado no válido")

    # Utilizar SQLAlchemy para filtrar registros basados en el campo y valor dados
    query = db.query(Ciudad).filter(getattr(Ciudad, field) == value)
    resultados = query.all()

    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron registros que coincidan con el filtro")

    return resultados