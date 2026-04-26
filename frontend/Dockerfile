# Imagen con version fija
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia la carpeta html dentro de la imagen
COPY html/ ./html/

# Se pone dentro de la carpeta copiada
WORKDIR /app/html

# Expone el puerto
EXPOSE 8080

# Comando para levantar el servidor
CMD ["python3", "-m", "http.server", "8080"]