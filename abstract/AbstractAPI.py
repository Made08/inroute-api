from typing import Any, List, Type, TypeVar, Generic
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

T = TypeVar("T", bound=BaseModel)  # Definición del tipo genérico

class AbstractAPI(Generic[T]):
    def __init__(self, model: Type[T], db: Session):
        self.model = model
        self.db = db

    def create(self, obj: T) -> T:
        new_obj = self.model(**obj.dict())
        self.db.add(new_obj)
        self.db.commit()
        self.db.refresh(new_obj)
        return new_obj

    def get(self, obj_id: Any) -> T:
        obj = self.db.query(self.model).get(obj_id)
        if obj is None:
            raise HTTPException(
                status_code=404,
                detail=f"{self.model.__name__} with ID {obj_id} not found"
            )
        return obj

    def update(self, obj_id: Any, obj: T) -> T:
        existing_obj = self.db.query(self.model).get(obj_id)
        if existing_obj is None:
            raise HTTPException(
                status_code=404,
                detail=f"{self.model.__name__} with ID {obj_id} not found"
            )
        for key, value in obj.dict().items():
            setattr(existing_obj, key, value)
        self.db.commit()
        self.db.refresh(existing_obj)
        return existing_obj

    def delete(self, obj_id: Any) -> None:
        obj = self.db.query(self.model).get(obj_id)
        if obj is None:
            raise HTTPException(
                status_code=404,
                detail=f"{self.model.__name__} with ID {obj_id} not found"
            )
        self.db.delete(obj)
        self.db.commit()

    def filter(self, field: str, value: Any) -> List[T]:
        # Verifica si el campo existe en el modelo
        if not hasattr(self.model, field):
            raise HTTPException(
                status_code=400,
                detail=f"The field '{field}' does not exist in the model {self.model.__name__}"
            )
        
        # Realiza la consulta filtrando por el campo y valor proporcionados
        objs = self.db.query(self.model).filter(getattr(self.model, field) == value).all()
        
        # Verifica si se encontraron objetos y devuelve el resultado
        if not objs:
            raise HTTPException(
                status_code=404,
                detail=f"No {self.model.__name__} found with {field} = {value}"
            )
        return objs