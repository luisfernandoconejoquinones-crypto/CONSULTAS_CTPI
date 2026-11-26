
from flask import Blueprint, jsonify, current_app

cantidad_power_bi_bp = Blueprint("cantidad_power_bi", __name__)

@cantidad_power_bi_bp.route("/api/cantidadPowerBICertificados")
def cantidad_power_bi():
    aprendices = current_app.config["aprendices"]

    cantidad = aprendices.count_documents({
        "PROGRAMA": {
            "$regex": r"^VISUALIZACION DE DATOS USANDO POWER BI\.?$",
            "$options": "i"
        },
        "ESTADO_APRENDIZ": {
            "$regex": "^CERTIFICADO$",
            "$options": "i"
        }
    })

    return jsonify({
        "Programa": "VISUALIZACION DE DATOS USANDO POWER BI",
        "Estado": "CERTIFICADO",
        "Cantidad": cantidad
    })
