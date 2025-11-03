from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from .models import Producto
from .serializers import ProductoSerializer
from .decorators import valida_datos

# Create your views here.

# Vista para obtener listado y creacion de productos
# Maneja las peticiones GET y POST
class ListaProductosView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    # Metodo para crear un producto
    @valida_datos
    def post(self, request, *args, **kwargs):
        # Validacion de valores opcionales
        descripcion_data = request.data.get("descripcion", "")
        disponible_data = request.data.get("disponible", True)
        # Creacion del objeto en la BD
        producto = Producto.objects.create(
            nombre=request.data["nombre"],
            descripcion=descripcion_data,
            precio=request.data["precio"],
            disponible = disponible_data
        )
        return Response(
            data=ProductoSerializer(producto).data,
            status=status.HTTP_201_CREATED
        )


# Vista para detalles de producto por ID
# Maneja las peticiones GET, PUT y DELETE
class DetalleProductoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    # Metodo para obtener un producto
    def get(self, request, *args, **kwargs):
        try:
            producto = self.queryset.get(pk=kwargs["pk"])
            return Response(ProductoSerializer(producto).data)
        except Producto.DoesNotExist:
            return Response(
                data={
                    "mesage": "NO existe el producto con ID {}".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    # Metodo para eliminar un producto
    def delete(self, request, *args, **kwargs):
        try:
            producto = self.queryset.get(pk=kwargs["pk"])
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response(
                data={
                    "mesage": "NO existe el producto con ID {}".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND)
    
    # Metodo para actualizar un producto
    @valida_datos
    def put(self, request, *args, **kwargs):
        try:
            # Obtiene el producto con ID indicado
            producto = self.queryset.get(pk=kwargs["pk"])
            serializer = ProductoSerializer()
            # Actualiza producto en la BD
            produto_updt = serializer.update(producto, request.data)
            return Response(ProductoSerializer(produto_updt).data)
        except Producto.DoesNotExist:
            return Response(data={
                "mesage": "NO existe el producto con ID {}".format(kwargs["pk"])
            }, 
            status=status.HTTP_404_NOT_FOUND)