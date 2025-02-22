# Imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar Flask con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
