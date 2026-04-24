from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

# Configuración de BD usando las variables de tu archivo .env
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "database"),
    "database": os.getenv("DB_NAME", "teamboard_db"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASS", "admin_pass")
}

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "backend"}), 200

@app.route('/api/team', methods=['GET'])
def get_team():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT nombre, apellido, legajo, feature, servicio, estado FROM members;")
        rows = cur.fetchall()
        team = [{"nombre": r[0], "apellido": r[1], "legajo": r[2], "feature": r[3], "servicio": r[4], "estado": r[5]} for r in rows]
        cur.close()
        conn.close()
        return jsonify(team)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
