from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from .models import Producto
from .serializers import ProductoSerializer
from .decorators import valida_datos

# Create your views here.

# Vista para obtener listado de productos
class ListaProductosView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para detalles de producto por ID
# Maneja las peticiones GET, PUT y DELETE
class DetalleProductoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

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
    
    @valida_datos
    def put(self, request, *args, **kwargs):
        try:
            producto = self.queryset.get(pk=kwargs["pk"])
            serializer = ProductoSerializer()
            produto_updt = serializer.update(producto, request.data)
            return Response(ProductoSerializer(produto_updt).data)
        except Producto.DoesNotExist:
            return Response(data={
                "mesage": "NO existe el producto con ID {}".format(kwargs["pk"])
            }, 
            status=status.HTTP_404_NOT_FOUND)