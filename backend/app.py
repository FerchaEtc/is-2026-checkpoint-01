from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os
import requests

app = Flask(__name__)
CORS(app)

SERVICE_URLS = {
    "frontend:8080": "http://frontend:8080/",
    "backend:5000": "http://backend:5000/api/health",
    "db": "db",
    "compose / repo": None,
    "portainer:9000": "http://portainer:9000/api/status",
    "pgadmin:5050": "http://pgadmin:5050/"
}

# Configuración de BD usando las variables los archivos .env
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "database": os.getenv("DB_NAME", "teamboard_db"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASS", "admin_pass")
}

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "backend"}), 200

@app.route('/api/team', methods=['GET'])
def get_team():
    def check_service_status(servicio):
        if servicio == "db":
            try:
                conn = psycopg2.connect(**DB_CONFIG)
                conn.close()
                return "online"
            except:
                return "offline"
        
        url = SERVICE_URLS.get(servicio)
        if not url:
            return "unknown"
        try:
            response = requests.get(url, timeout=3)
            return "online" if response.status_code == 200 else "offline"
        except:
            return "offline"

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT nombre, apellido, legajo, feature, servicio FROM members;")
        rows = cur.fetchall()
        team = []
        for r in rows:
            servicio = r[4]
            estado = check_service_status(servicio)
            team.append({
                "nombre": r[0],
                "apellido": r[1],
                "legajo": r[2],
                "feature": r[3],
                "servicio": servicio,
                "estado": estado
            })
        cur.close()
        conn.close()
        return jsonify(team)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
