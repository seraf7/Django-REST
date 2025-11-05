# ANEXO endpoints

El modelo de datos generado contempla la siguiente definicion de un Producto

|Campo|Tipo|Obligatorio|Restricciones|
|-----|----|-----------|-------------|
|id         |entero  |NA|autogenerado         |
|nombre     |string  |Si|maximo 30 caracteres |
|descripcion|string  |No|maximo 100 caracteres|
|precio     |decimal |Si|Valor mayor a 0      |
|disponible |booleano|No|                     |

## Endpoints soportados

|Método|Endpoint|Función|Referencia|
|------|--------|-------|----------|
|GET   |`/api/productos/`     |Listar todos los productos    |[documentacion](#listar-productos)|
|POST  |`/api/productos/`     |Crear un producto             |[documentacion](#crear-producto)|
|GET   |`/api/productos/{id}/`|Obtener un producto dado su ID|[documentacion](#obtener-producto)|
|PUT   |`/api/productos/{id}/`|Actualizar un producto        |[documentacion](#actualizar-producto)|
|DELETE|`/api/productos/{id}/`|Eliminar un producto          |[documentacion](#eliminar-producto)|


## Listar productos
Recupera listado de productos que han sido dados de alta en el sistema

|GET   |`/api/productos/`|
|------|--------|

### Respuestas

#### Codigo 200 OK
Se recibe un arreglo con los productos existentes en el sistema

#### Ejemplo de respuesta
Arreglo con la definición de cada producto existente

``` json
[
  {
    "id": 1,
    "nombre": "Tijeritas",
    "descripcion": "tijeras escolares",
    "precio": "30.90",
    "disponible": false
  },
  {
    "id": 2,
    "nombre": "PlayDooh",
    "descripcion": "plastilina",
    "precio": "30.90",
    "disponible": true
  },
  ...
  {
    "id": n,
    "nombre": "Producto N",
    "descripcion": "descripcion",
    "precio": "30.90",
    "disponible": true
  }
]
```
[Endpoints soportados](#endpoints-soportados)

## Crear producto
Da de alta un producto en el sistema con los parametros recibidos

|POST  |`/api/productos/`|
|------|--------|

### Solicitud
Se envia a través de un JSON los campos que definirán al producto. Se requiere como mínimo los valores definidos como obligatorios y que cumplan con las restricciones

#### Ejemplo de cuerpo de la solicitud
``` json
{
  "nombre": "Producto N",
  "descripcion": "Nuevo producto",
  "precio": 30.90, 
  "disponible": true
}
```

### Respuestas

#### Codigo 201 CREATED
El producto es dado de alta de manera exitosa en el sistema

#### Ejemplo de respuesta
Se recibe el producto dado de alta con sus cinco campos correspondientes

``` json
{
  "id": 11,
  "nombre": "Producto N",
  "descripcion": "Nuevo producto",
  "precio": "30.90",
  "disponible": true
}
```

#### Codigo 400 BAD REQUEST
El producto no es dado de alta debido a que la solicitud no contiene datos validos para la operación

#### Ejemplo de respuesta
Se recibe el mensaje con el error correspondiente en los datos

Ejemplo de error en el precio
``` json
{
  "mesage": "El precio debe ser mayor a 0"
}
```
Ejemplo de error por campos faltantes
``` json
{
  "mesage": "Los campos nombre y precio son requeridos"
}
```
[Endpoints soportados](#endpoints-soportados)

## Obtener producto
Recupera un producto del sistema dado su ID

|GET   |`/api/productos/{id}/`|
|------|--------|

### Solicitud
Se envia a través del endpoint el ID del producto que se desea recuperar

#### Ejemplo de solicitud
``` 
http://127.0.0.1:8000/api/productos/11/
```

### Respuestas

#### Codigo 200 OK
Se recibe el producto que tiene el ID recibido con sus cinco campos correspondientes

#### Ejemplo de respuesta
``` json
{
  "id": 11,
  "nombre": "Producto N",
  "descripcion": "Nuevo producto",
  "precio": "30.90",
  "disponible": true
}
```

#### Codigo 404 NOT FOUND
Se recibe el mensaje de error por producto no existente

#### Ejemplo de respuesta
``` json
{
  "mesage": "NO existe el producto con ID N"
}
```
[Endpoints soportados](#endpoints-soportados)

## Actualizar producto
Actualiza un producto del sistema dado su ID

|PUT   |`/api/productos/{id}/`|
|------|--------|

### Solicitud
Se envia a través de un JSON los campos que se modificaran en el producto. Se requiere como mínimo los valores definidos como obligatorios y que cumplan con las restricciones

#### Ejemplo de cuerpo de la solicitud
``` json
{
  "nombre": "Producto N",
  "descripcion": "Producto modificado",
  "precio": 30.9
}
```

### Respuestas

#### Codigo 200 OK
Se actualiza correctamente el producto, se recibe el producto que tiene el ID recibido con sus cinco campos correspondientes actualizados

#### Ejemplo de respuesta

``` json
{
  "id": 11,
  "nombre": "Producto N",
  "descripcion": "Producto modificado",
  "precio": "30.90",
  "disponible": false
}
```

#### Codigo 404 NOT FOUND
Se recibe el mensaje de error por producto no existente

#### Ejemplo de respuesta
``` json
{
  "mesage": "NO existe el producto con ID N"
}
```

#### Codigo 400 BAD REQUEST
El producto no es dado de alta debido a que la solicitud no contiene datos validos para la operación

#### Ejemplo de respuesta
Se recibe el mensaje con el error correspondiente en los datos

Ejemplo de error en el precio
``` json
{
  "mesage": "mensaje de error"
}
```
[Endpoints soportados](#endpoints-soportados)

## Eliminar producto
Elimina un producto del sistema dado su ID

|DELETE|`/api/productos/{id}/`|
|------|--------|

#### Ejemplo de solicitud
``` 
http://127.0.0.1:8000/api/productos/11/
```

### Respuestas

#### Codigo 204 NO CONTENT
El producto es eliminado de manera exitosa del sistema

#### Ejemplo de respuesta
No se reciben mensajes de respuesta

#### Codigo 404 NOT FOUND
Se recibe el mensaje de error por producto no existente, no se hacen cambios en el sistema

#### Ejemplo de respuesta
``` json
{
  "mesage": "NO existe el producto con ID N"
}
```
[Endpoints soportados](#endpoints-soportados)