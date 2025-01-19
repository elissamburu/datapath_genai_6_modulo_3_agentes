# Usa una imagen base ligera de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto en el que la aplicación estará disponible
EXPOSE 8080

# Comando predeterminado para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]