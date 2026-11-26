from flask import Blueprint, jsonify, current_app

estado_bp = Blueprint("estado", __name__)

@estado_bp.route("/api/aprendicesPorEstado")
def aprendicesPorEstado():
    aprendices = current_app.config["aprendices"]

    estados = [
        "Formación",
        "Por certificar",
        "Certificado",
        "Retiro Voluntario",
        "Traslado",
        "Aplazado",
        "Cancelado"
    ]

    resultado = list(aprendices.find(
        {
            "FICHA": 3312932,
            "ESTADO_APRENDIZ": {
                "$in": estados
            }
        },
        {
            "_id": 0,
            "FICHA": 1,
            "PROGRAMA": 1,
            "NUMERO_DOCUMENTO": 1,
            "NOMBRE": 1,
            "PRIMER_APELLIDO": 1,
            "SEGUNDO_APELLIDO": 1,
            "ESTADO_APRENDIZ": 1
        }
    ).sort([
        ("ESTADO_APRENDIZ", 1),
        ("PRIMER_APELLIDO", 1)
    ]))

    aprendices_por_estado = {
        estado: [] for estado in estados
    }

    for aprendiz in resultado:
        estado = aprendiz["ESTADO_APRENDIZ"]
        aprendices_por_estado[estado].append(aprendiz)

    resultado_final = []

    for estado in estados:
        resultado_final.append({
            "Estado": estado,
            "Cantidad": len(aprendices_por_estado[estado]),
            "Aprendices": aprendices_por_estado[estado]
        })

    return jsonify({
        "Ficha": 3312932,
        "Total de aprendices": len(resultado),
        "Aprendices por estado": resultado_final
    })