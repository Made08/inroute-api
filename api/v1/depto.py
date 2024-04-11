from flask import Blueprint, jsonify
from models import Depto

depto_v1_bp = Blueprint('depto_v1', __name__, url_prefix='/v1/depto')


@depto_v1_bp.route('/', methods=['GET'])
def obtener_deptos():
    deptos = Depto.query.all()
    resultado = [{
            'id': depto.id,
            'nombre': depto.nombre,
            'pais_id': depto.pais_id,
            'estado': depto.estado,
            'fecha_registro': depto.fecha_registro.isoformat(),
            'fecha_actualizacion': depto.fecha_actualizacion.isoformat(),
            'usuario_id': depto.usuario_id,
            'ip_address': depto.ip_address
    } for depto in deptos]
    return jsonify(resultado)

@depto_v1_bp.route('/<depto_id>', methods=['GET'])
def obtener_depto(depto_id):
    depto = Depto.query.get(depto_id)
    if not depto:
        return jsonify({'mensaje': 'depto no encontrado'}), 404

    resultado = {
            'id': depto.id,
            'nombre': depto.nombre,
            'pais_id': depto.pais_id,
            'estado': depto.estado,
            'fecha_registro': depto.fecha_registro.isoformat(),
            'fecha_actualizacion': depto.fecha_actualizacion.isoformat(),
            'usuario_id': depto.usuario_id,
            'ip_address': depto.ip_address
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar países si es necesario.
