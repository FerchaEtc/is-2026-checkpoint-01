FROM python:3.12-slim

# Por seguridad, creamos un usuario que no sea root
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/* && useradd -m appuser
WORKDIR /app

# Copiamos e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY app.py .

# Usamos el usuario seguro
USER appuser

EXPOSE 5000

# El comando para arrancar la API
CMD ["python", "app.py"]
