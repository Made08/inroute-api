from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.String(3), primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    indicativo_telefonico = db.Column(db.Numeric(4), nullable=False)
    estado = db.Column(db.Numeric(1), nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    usuario_id = db.Column(db.String(10), nullable=True)
    ip_address = db.Column(db.String(15), nullable=True)
    def __repr__(self):
        return f"<Pais(id='{self.id}', nombre='{self.nombre}', indicativo_telefonico={self.indicativo_telefonico}, estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', usuario_id='{self.usuario_id}', ip_address='{self.ip_address}')>"


class Depto(db.Model):
    __tablename__ = 'depto'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.String(2), primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    pais_id = db.Column(db.String(3), nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    usuario_id = db.Column(db.String(10), nullable=True)
    ip_address = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        return f"<Depto(id='{self.id}', nombre='{self.nombre}', pais_id={self.pais_id}, estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', usuario_id='{self.usuario_id}', ip_address='{self.ip_address}')>"


class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id = db.Column(db.String(3), primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    depto_id = db.Column(db.String(2), nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    usuario_id = db.Column(db.String(10), nullable=True)
    ip_address = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        return f"<Ciudad(id='{self.id}', nombre='{self.nombre}', depto_id='{self.depto_id}', estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', usuario_id='{self.usuario_id}', ip_address='{self.ip_address}')>"
