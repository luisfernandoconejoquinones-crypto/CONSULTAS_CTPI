
from flask import Blueprint, jsonify, current_app

certificados_bp = Blueprint("certificados", __name__)

@certificados_bp.route("/api/certificados/<programa>")
def certificados(programa):
    aprendices = current_app.config["aprendices"]

    resultado = list(aprendices.find(
        {
            "PROGRAMA": programa,
            "ESTADO_APRENDIZ": "Certificado"
        },
        {
            "_id": 0,
            "FICHA": 1,
            "NOMBRE": 1,
            "PRIMER_APELLIDO": 1,
            "SEGUNDO_APELLIDO": 1
        }
    ))

    return jsonify({
        "Aprendices_Certificados": resultado,
        "Programa": programa
    })
