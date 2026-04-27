# Imagen con version fija
FROM python:3.12-slim

# Instala curl para healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia la carpeta html dentro de la imagen
COPY html/ ./html/

# Se pone dentro de la carpeta copiada
WORKDIR /app/html

# Expone el puerto
EXPOSE 8080

# Healthcheck
HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD curl -f http://localhost:8080/ || exit 1

# Comando para levantar el servidor
CMD ["python3", "-m", "http.server", "8080"]