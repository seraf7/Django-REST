from rest_framework.response import Response
from rest_framework.views import status

def valida_datos(funcion):
    def validador(*args, **kwargs):
        # Recupera datos contenidos en la solicitud
        nombre = args[0].request.data.get("nombre", "")
        precio = args[0].request.data.get("precio", "")
        # Valida que los campos no esten vacios
        if(not nombre or not precio):
            return Response(data={
                "mesage": "Los campos nombre y precio son requeridos"
            }, status=status.HTTP_400_BAD_REQUEST)
        # Valida que llegue un precio valido
        if precio:
            precio_f = float(precio)
            if(precio_f<=0):
                return Response(data={
                    "mesage": "El precio debe ser mayor a 0"
                }, status=status.HTTP_400_BAD_REQUEST)
        return funcion(*args, **kwargs)
    return validador