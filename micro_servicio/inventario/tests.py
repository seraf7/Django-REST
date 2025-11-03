import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Producto
from .serializers import ProductoSerializer

# Test de endpoint GET para obtener todos los Productos
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def crea_producto(nombre="", descripcion="", precio=0):
        if(nombre!="" and descripcion!="" and precio>0):
            Producto.objects.create(nombre=nombre, 
                                    descripcion=descripcion, precio=precio)
    
    # Metodo para la carga inicial de productos
    def setUp(self):
        self.crea_producto("Tijeras", "tijeras escolares", 25.5)
        self.crea_producto("Gommy", "Resistol en barra", 15.3)
        self.id_valido = 1
        self.id_borrado = 2
        self.id_invalido = 50
        self.datos_validos = {"id": 1,
                              "nombre": "PlayDooh", 
                              "descripcion": "Plastilina", 
                              "precio": "30.40",
                              "disponible": True}
        self.datos_invalidos_1 = {"nombre": "", "descripcion": "Plastilina", "precio": 30.40}
        self.datos_invalidos_2 = {"nombre": "PlayDooh", "descripcion": "Plastilina", "precio": -30.40}
    
# Caso de prueba para obtener todos los productos 
# (GET) /api/productos/
class GetProductosTest(BaseViewTest):
    def test_get_productos(self):
        # Llamada al endpoint
        response = self.client.get(
            reverse("productos-all")
        )
        # Fetch de los datos
        expected = Producto.objects.all()
        serialized = ProductoSerializer(expected, many=True)
        # Comparacion de las respuestas obtenidas
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Caso de prueba para obtener un producto por su ID 
# (GET) /api/productos/{id}/
class GetProductoPorIDTest(BaseViewTest):
    def test_get_producto(self):
        # Obtiene objeto de BD con ID indicado
        expected = Producto.objects.get(pk=self.id_valido)
        serialized = ProductoSerializer(expected)
        # Peticion GET a la API con ID valido
        response = self.client.get(
            reverse("producto-detalle", kwargs={"pk": self.id_valido})
        )
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Peticion GET a la API con ID invalido
        response = self.client.get(
            reverse("producto-detalle", kwargs={"pk": self.id_invalido})
        )
        self.assertEqual(response.data["mesage"],
                         "NO existe el producto con ID {}".format(self.id_invalido))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Caso de prueba para borrar un producto con su ID
# (DELETE) /api/productos/{id}/
class DeleteProductoTest(BaseViewTest):
    def test_delete_producto(self):
        # Peticion DELETE a la API con ID valido
        response = self.client.delete(
            reverse("producto-detalle", kwargs={"pk": self.id_borrado})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Peticion DELETE a la API con ID invalido
        response = self.client.delete(
            reverse("producto-detalle", kwargs={"pk": self.id_invalido})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Caso de prueba para actualizar un producto con su ID
# (PUT) /api/productos/{id}/
class UpdateProductoTest(BaseViewTest):
    def test_update_producto(self):
        # Peticion PUT a la API con datos validos
        response = self.client.put(
            reverse("producto-detalle", kwargs={"pk": self.id_valido}),
            data=json.dumps(self.datos_validos),
            content_type='application/json'
        )
        self.assertEqual(response.data, self.datos_validos)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Peticion PUT a la API con datos incompletos
        response = self.client.put(
            reverse("producto-detalle", kwargs={"pk": self.id_valido}),
            data=json.dumps(self.datos_invalidos_1),
            content_type='application/json'
        )
        self.assertEqual(response.data["mesage"], "Los campos nombre y precio son requeridos")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Peticion PUT a la API con precio invalido
        response = self.client.put(
            reverse("producto-detalle", kwargs={"pk": self.id_valido}),
            data=json.dumps(self.datos_invalidos_2),
            content_type='application/json'
        )
        self.assertEqual(response.data["mesage"], "El precio debe ser mayor a 0")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)