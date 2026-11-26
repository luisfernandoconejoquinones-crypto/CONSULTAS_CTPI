
from flask import Blueprint, jsonify, current_app

por_certificar_bp = Blueprint("por_certificar", __name__)

@por_certificar_bp.route("/api/porCertificar/<ficha>/<cantidad>")
def por_certificar(ficha, cantidad):
    aprendices = current_app.config["aprendices"]

    resultado = list(aprendices.find(
        {
            "FICHA": int(ficha),
            "ESTADO_APRENDIZ": "Por certificar"
        },
        {
            "_id": 0,
            "FICHA": 1,
            "PROGRAMA": 1,
            "NUMERO_DOCUMENTO": 1,
            "NOMBRE": 1,
            "PRIMER_APELLIDO": 1,
            "SEGUNDO_APELLIDO": 1
        }
    ).sort("PRIMER_APELLIDO", -1).limit(int(cantidad)))

    return jsonify({
        "Cantidad de Aprendices por Certificar": resultado
    })
