# Usa una imagen base de Python
FROM python:3.13-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Crea un volumen
RAILWAY_VOLUME_NAME : hola
RAILWAY_VOLUME_MOUNT_PATH : /hola

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["/bin/sh", "-c", "python manage.py migrate && uvicorn PruebasDespliegue.asgi:application --host 0.0.0.0 --port 8000"]