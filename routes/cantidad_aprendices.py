
from flask import Blueprint, jsonify, current_app

cantidad_bp = Blueprint("cantidad", __name__)

@cantidad_bp.route("/api/cantidadAprendices")
def cantidadAprendices():
    aprendices = current_app.config["aprendices"]

    cantidad = aprendices.count_documents({})

    return jsonify({
        "CantidadAprendices": cantidad
    })
