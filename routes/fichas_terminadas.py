
from flask import Blueprint, jsonify, current_app

fichas_terminadas_bp = Blueprint("fichas_terminadas", __name__)

@fichas_terminadas_bp.route("/api/fichasTerminadas/<programa>")
def fichas_terminadas(programa):
    aprendices = current_app.config["aprendices"]

    resultado = list(aprendices.find(
        {
            "PROGRAMA": programa,
            "ESTADO_FICHA": "Terminada por unificación"
        },
        {
            "_id": 0,
            "FICHA": 1,
            "NUMERO_DOCUMENTO": 1,
            "NOMBRE": 1,
            "PRIMER_APELLIDO": 1,
            "SEGUNDO_APELLIDO": 1
        }
    ))

    return jsonify({
        "Programa": programa,
        "Aprendices": resultado
    })
