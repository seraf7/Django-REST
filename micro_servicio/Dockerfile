# Imagen de Python
FROM python:3.11

# Vaeriable de ambiente para enviar salidas a terminal
ENV PYTHONBUFFERED 1

# Directorio para el contenedor del proyecto
RUN mkdir /servicio_producto

# Configuracion del directorio de trabajo
WORKDIR /servicio_producto

# Copia de archivos al contenedor
ADD . /servicio_producto/

# Instalacion de paquetes requeridos
RUN pip install -r requirements.txt