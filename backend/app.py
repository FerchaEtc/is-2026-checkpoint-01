import os
from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configuración de la conexión usando variables de entorno
# Estas variables las definirá el coordinador en el docker-compose.yml
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'db'),
            database=os.getenv('DB_NAME', 'teamboard'),
            user=os.getenv('DB_USER', 'admin'),
            password=os.getenv('DB_PASSWORD', 'admin123')
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

@app.route('/api/health')
def health():
    """Endpoint para el HEALTHCHECK de Docker"""
    return jsonify({"status": "up", "service": "backend"}), 200

@app.route('/api/team')
def get_team():
    """Endpoint que lee los integrantes de la base de datos"""
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "No se pudo conectar a la DB"}), 500
    
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT name, feature, status FROM members;')
        team = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(team)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # El puerto 5000 es el requerido por la cátedra
    app.run(host='0.0.0.0', port=5000)