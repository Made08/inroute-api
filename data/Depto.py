from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Depto(Base):
    __tablename__ = "depto"
    __table_args__ = {'schema': 'public'}
    
    id = Column(String(2), primary_key=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    pais_id = Column(String(3), ForeignKey("pais.id"), nullable=False)
    estado = Column(Integer, default=1)
    fecha_registro = Column(TIMESTAMP(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), onupdate=text('CURRENT_TIMESTAMP'))
    usuario_id = Column(String(10), nullable=True)
    ip_address = Column(String(15), nullable=True)

    pais = relationship("Pais", back_populates="deptos")
