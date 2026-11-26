
from flask import Blueprint, jsonify, current_app

programas_bp = Blueprint("programas", __name__)

@programas_bp.route("/api/programas/<nivel>")
def programas_por_nivel(nivel):
    aprendices = current_app.config["aprendices"]

    programas = aprendices.distinct(
        "PROGRAMA",
        {"NIVEL_DE_FORMACION": nivel}
    )

    return jsonify({
        "nivel de formación": nivel,
        "programas": sorted(programas)
    })
