from sqlalchemy import Column, String, Numeric, Integer, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pais(Base):
    __tablename__ = "pais"

    id = Column(String(3), primary_key=True, nullable=False)
    nombre = Column(String(40), nullable=False)
    indicativo_telefonico = Column(Numeric(4), nullable=False)
    estado = Column(Numeric(1), default=1)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    # Relación con la tabla Depto
    deptos = relationship('Depto', back_populates='pais')

class Depto(Base):
    __tablename__ = "depto"

    id = Column(String(2), primary_key=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    pais_id = Column(String(3), ForeignKey("pais.id"), nullable=False)
    estado = Column(Integer, default=1)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    pais = relationship('Pais', back_populates='deptos')