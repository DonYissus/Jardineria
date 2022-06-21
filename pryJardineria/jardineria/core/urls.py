from unicodedata import name
from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import catalogo, eliminar_producto, home, listado_producto, login, modificar_producto, nuevo_producto, quienessomos, registro_usuario, seguimiento, sign

from .views import ProductoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos',ProductoViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('catalogo/', catalogo, name="catalogo"),
    path('seguimiento/', seguimiento, name="seguimiento"),
    path('login/', login, name="login"),
    path('sign/', sign, name="sign"),
    path('listado-productos/', listado_producto, name="listado_productos"),
    path('nuevo-producto/', nuevo_producto, name="nuevo_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('api/', include(router.urls)),
    
]
