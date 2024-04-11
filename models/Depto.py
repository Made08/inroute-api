from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class DeptoBase(BaseModel):
    id: str
    nombre: str
    pais_id: str
    estado: Optional[int] = 1
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]
    usuario_id: Optional[str]
    ip_address: Optional[str]

    class Config:
        from_attributes = True
