from django.urls import path
from .views import ListaProductosView, DetalleProductoView

urlpatterns = [
    path('productos/<int:pk>/', DetalleProductoView.as_view(), name="producto-detalle"),
    path('productos/', ListaProductosView.as_view(), name="productos-all"),
    
]