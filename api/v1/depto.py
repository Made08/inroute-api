from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.DataModel import Depto
from models.Depto import DeptoBase
from config import SessionLocal
from typing import List, Optional

# Crear un enrutador con el prefijo "/v1/pais"
router = APIRouter(prefix="/v1/depto", tags=["Depto"])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new Depto
@router.post("/", response_model=DeptoBase)
def create_depto(depto: DeptoBase, db: Session = Depends(get_db)):
    db_depto = Depto(**depto.dict())
    db.add(db_depto)
    db.commit()
    db.refresh(db_depto)
    return db_depto

# Read a Depto by id
@router.get("/{id}", response_model=DeptoBase)
def read_depto(id: str, db: Session = Depends(get_db)):
    depto = db.query(Depto).filter(Depto.id == id).first()
    if not depto:
        raise HTTPException(status_code=404, detail="Depto not found")
    return depto

# Update a Depto by id
@router.put("/{id}", response_model=DeptoBase)
def update_depto(id: str, depto: DeptoBase, db: Session = Depends(get_db)):
    db_depto = db.query(Depto).filter(Depto.id == id).first()
    if not db_depto:
        raise HTTPException(status_code=404, detail="Depto not found")
    
    for key, value in depto.dict().items():
        setattr(db_depto, key, value)
        
    db.commit()
    db.refresh(db_depto)
    return db_depto

# Delete a Depto by id
@router.delete("/{id}")
def delete_depto(id: str, db: Session = Depends(get_db)):
    db_depto = db.query(Depto).filter(Depto.id == id).first()
    if not db_depto:
        raise HTTPException(status_code=404, detail="Depto not found")
    
    db.delete(db_depto)
    db.commit()
    return {"detail": "Depto deleted"}

# Read all Deptos
@router.get("/", response_model=List[DeptoBase])
def read_deptos(db: Session = Depends(get_db)):
    return db.query(Depto).all()

@router.get("/filter/{field}/{value}", response_model=List[DeptoBase])
def filter_deptos(
        field: str,  # Argumento sin valor predeterminado
    value: str,  # Argumento sin valor predeterminado
    db: Session = Depends(get_db)  # Argumento con valor predeterminado (dependencia)
):
    # Valida existencia del campo
    if not hasattr(Depto, field):
        raise HTTPException(status_code=400, detail="Campo de filtrado no válido")

    # Utilizar SQLAlchemy para filtrar registros basados en el campo y valor dados
    query = db.query(Depto).filter(getattr(Depto, field) == value)
    resultados = query.all()
    
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron registros que coincidan con el filtro")

    return resultados
