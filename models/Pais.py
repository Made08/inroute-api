from sqlalchemy import Column, String, Numeric, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pais(Base):
    __tablename__ = "pais"
    __table_args__ = {'schema': 'public'}

    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(40), nullable=False)
    indicativo_telefonico = Column(Numeric(4), nullable=False)
    estado = Column(Numeric(1), default=1)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)