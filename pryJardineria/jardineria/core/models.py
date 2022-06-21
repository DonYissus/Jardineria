from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    TipoProducto = models.ForeignKey(TipoProducto, on_delete=CASCADE)
    DetalleProducto = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
        