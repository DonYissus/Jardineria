from django.contrib import admin
from .models import TipoProducto, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'TipoProducto']
    search_fields = ['nombre', 'TipoProducto']
    list_filter = ['TipoProducto']
    list_per_page = 10
admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)