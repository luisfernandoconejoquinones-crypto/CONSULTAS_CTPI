from flask import Blueprint, jsonify, current_app

complementaria_bp = Blueprint("complementaria", __name__)

@complementaria_bp.route("/api/programasComplementariaVirtual")
def programasComplementariaVirtual():
    aprendices = current_app.config["aprendices"]

    resultado = aprendices.distinct(
        "PROGRAMA",
        {
            "NIVEL_DE_FORMACION": "COMPLEMENTARIA VIRTUAL"
        }
    )

    resultado = sorted(resultado)

    return jsonify({
        "Nivel de formación": "COMPLEMENTARIA VIRTUAL",
        "Cantidad de programas": len(resultado),
        "Programas": resultado
    })