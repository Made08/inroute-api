from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CiudadBase(BaseModel):
    id: str
    nombre: str
    depto_id: str
    estado: Optional[int] = 1
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None
    usuario_id: Optional[str] = None
    ip_address: Optional[str] = None

    class Config:
        from_attributes = True
