
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

from routes.por_certificar import por_certificar_bp
app.register_blueprint(por_certificar_bp)

from routes.fichas_terminadas import fichas_terminadas_bp
app.register_blueprint(fichas_terminadas_bp)

from routes.aprendices_power_bi import power_bi_bp
app.register_blueprint(power_bi_bp)


from routes.cantidad_power_bi import cantidad_power_bi_bp
app.register_blueprint(cantidad_power_bi_bp)

from routes.aprendices_por_estado import estado_bp
app.register_blueprint(estado_bp)

from routes.programas_complementaria_virtual import complementaria_bp
app.register_blueprint(complementaria_bp)

@app.route("/")
def inicio():
    try:
        cliente.admin.command("ping")
        return "¡Conexion con MongoDB exitosa!"
    except Exception as e:
        return f"Error de conexion: {e}"


if __name__ == "__main__":
    app.run(debug=True)
