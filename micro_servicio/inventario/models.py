from django.db import models

# Create your models here.

# Definicion del modelo Producto
class Producto(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=30,
        null=False
    )
    descripcion = models.TextField(
        blank=True,
        max_length=100
    )
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False
    )
    disponible = models.BooleanField(
        default=True,
        null=False
    )
