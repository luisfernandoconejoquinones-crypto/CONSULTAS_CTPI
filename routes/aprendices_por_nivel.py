
from flask import Blueprint, jsonify, current_app

nivel_bp = Blueprint("nivel", __name__)

@nivel_bp.route("/api/aprendicesPorNivel")
def aprendicesPorNivel():
    aprendices = current_app.config["aprendices"]

    resultado = aprendices.aggregate([
        {
            "$group": {
                "_id": "$NIVEL_DE_FORMACION",
                "cantidad": {"$sum": 1}
            }
        },
        {
            "$project": {
                "_id": 0,
                "nivel_formacion": "$_id",
                "cantidad": 1
            }
        },
        {
            "$sort": {"nivel_formacion": 1}
        }
    ])

    return jsonify(list(resultado))
