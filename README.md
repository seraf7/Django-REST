# Django-REST
Prueba de microservicio en Django REST Framework para la gestión de productos mediante una API

## Tecnologías usadas

* [Django](https://www.djangoproject.com/): framework para el desarrollo de aplicaciones web
* [Django REST Framework](https://www.django-rest-framework.org/): framework para el desarrolo de API sobre aplicaciones Django 
* [SQLite](https://sqlite.org/): motor de base de datos relaciones embebido

## Procedimiento de instalación
Posicionarse en el directorio de trabajo y realizar el clonado del repositorio

``` bash 
git clone https://github.com/seraf7/Django-REST.git
```

### Instalación local
1. Acceder al directorio de la aplicación en el repositorio
``` bash 
cd Django-REST/micro_servicio
```

2. Preparación del ambiente virtual
``` bash 
python3 -m venv micro_serv
source micro_serv/bin/activate
```

3. Instalación de paquetes requeridos
``` bash 
pip install -r requirements.txt
```

### Instalación con Docker
1. Comprobar que se tiene instalado `Docker` y `docker-compose` ejecutando los siguientes comandos
``` bash
docker -v
docker-compose -v
```

2. Una vez que se ha comprobado que se tiene instalado `Docker` y `docker-compose`, verificar que los servicios de `Docker` se encuentran habilitados
``` bash 
systemctl status docker
```

3. Comprobado que los servicios de `Docker` estan habilitados, acceder al directorio de la aplicación en el repositorio
``` bash 
cd Django-REST/micro_servicio
```

4. Ejecutar el siguiente comando para crear el contenedor y levantar el servidor dentro de `Docker` 
``` bash 
docker-compose up
```

5. En el navegador, acceder a la ruta [http://127.0.0.1:8000/api/productos/](http://127.0.0.1:8000/api/productos/) para comprobar que el servidor se encuentra activo

## Ejecución de migraciones
Para la ejecución de las migraciones, ejecutar los siguientes comandos estando posicionado en el directorio de la aplicación `Django-REST/micro_servicio`

``` bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Levantar el servidor
Para levantar el servidor, ejecutar el siguiente comando estando posicionado en el directorio de la aplicación `Django-REST/micro_servicio`

``` bash
python3 manage.py runserver
```

## Ejecución de pruebas
Para correr las pruebas, ejecutar el siguiente comando estando posicionado en el directorio de la aplicación `Django-REST/micro_servicio`

``` bash
python3 manage.py test
```

Se realiza la ejecución de seis casos de prueba, obteniendo una salida como la siguiente

``` console
(micro_serv) pc:Django-REST/micro_servicio$ python3 manage.py test
Found 6 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.059s

OK
Destroying test database for alias 'default'...
(micro_serv) pc:Django-REST/micro_servicio$
```

## Información sobre endpoints

|Método|Endpoint|Función|
|------|--------|-------|
|GET   |`/api/productos/`     |Listar todos los productos    |
|POST  |`/api/productos/`     |Crear un producto             |
|GET   |`/api/productos/{id}/`|Obtener un producto dado su ID|
|PUT   |`/api/productos/{id}/`|Actualizar un producto        |
|DELETE|`/api/productos/{id}/`|Eliminar un producto          |