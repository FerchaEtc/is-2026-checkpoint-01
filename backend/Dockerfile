FROM python:3.12-slim

# Crear usuario sin privilegios por seguridad
RUN useradd -m appuser
USER appuser
WORKDIR /home/appuser

# Copiar requirements primero para aprovechar el caché de capas
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY --chown=appuser:appuser . .

# HEALTHCHECK obligatorio apuntando a /api/health
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/api/health || exit 1

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
