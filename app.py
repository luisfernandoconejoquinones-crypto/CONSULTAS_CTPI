
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

cliente = MongoClient(os.getenv("MONGO_URI"))

db = cliente["CURSOS_CTPI_2026-FERNANDO"]
aprendices = db["APRENDICES_CONEJO"]
app.config["aprendices"] = aprendices

from routes.cantidad_aprendices import cantidad_bp
app.register_blueprint(cantidad_bp)

from routes.aprendices_por_nivel import nivel_bp
app.register_blueprint(nivel_bp)

from routes.programas import programas_bp
app.register_blueprint(programas_bp)

from routes.certificados import certificados_bp
app.register_blueprint(certificados_bp)


@app.route("/")
def inicio():
    try:
        cliente.admin.command("ping")
        return "¡Conexion con MongoDB exitosa!"
    except Exception as e:
        return f"Error de conexion: {e}"


if __name__ == "__main__":
    app.run(debug=True)
