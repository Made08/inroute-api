from flask import Blueprint, jsonify
from models import Ciudad

ciudad_v1_bp = Blueprint('ciudad_v1', __name__, url_prefix='/v1/ciudad')


@ciudad_v1_bp.route('/', methods=['GET'])
def obtener_ciudades():
    ciudades = Ciudad.query.all()
    resultado = [{
            'id': ciudad.id,
            'nombre': ciudad.nombre,
            'depto_id': ciudad.depto_id,
            'estado': ciudad.estado,
            'fecha_registro': ciudad.fecha_registro.isoformat(),
            'fecha_actualizacion': ciudad.fecha_actualizacion.isoformat(),
            'usuario_id': ciudad.usuario_id,
            'ip_address': ciudad.ip_address
    } for ciudad in ciudades]
    return jsonify(resultado)

@ciudad_v1_bp.route('/<ciudad_id>', methods=['GET'])
def obtener_ciudad(ciudad_id):
    ciudad = Ciudad.query.get(ciudad_id)
    if not ciudad:
        return jsonify({'mensaje': 'Ciudad no encontrada'}), 404
        
    resultado = {
        'id': ciudad.id,
        'nombre': ciudad.nombre,
        'depto_id': ciudad.depto_id,
        'estado': ciudad.estado,
        'fecha_registro': ciudad.fecha_registro.isoformat(),
        'fecha_actualizacion': ciudad.fecha_actualizacion.isoformat(),
        'usuario_id': ciudad.usuario_id,
        'ip_address': ciudad.ip_address
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar países si es necesario.
