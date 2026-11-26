
from flask import Blueprint, jsonify, current_app

power_bi_bp = Blueprint("power_bi", __name__)

@power_bi_bp.route("/api/aprendicesPowerBI")
def aprendices_power_bi():
    aprendices = current_app.config["aprendices"]

    resultado = list(aprendices.find(
        {
            "PROGRAMA": {
                "$regex": r"^VISUALIZACION DE DATOS USANDO POWER BI\.?$",
                "$options": "i"
            }
        },
        {
            "_id": 0,
            "PROGRAMA": 1,
            "FICHA": 1,
            "NOMBRE": 1,
            "PRIMER_APELLIDO": 1,
            "SEGUNDO_APELLIDO": 1
        }
    ))

    return jsonify({
        "Aprendices": resultado
    })
