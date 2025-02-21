# Imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar Flask
CMD ["python", "app.py"]
