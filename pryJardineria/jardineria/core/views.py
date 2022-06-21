from django.shortcuts import render, redirect
from core.forms import CustomUserForm, ProductoForm
from core.models import Producto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

from rest_framework import viewsets
from.serializers import ProductoSerializer

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')

def seguimiento(request):
    return render(request, 'core/seguimiento.html')

def login(request):
    return render(request, 'core/login.html')

def sign(request):
    return render(request, 'core/sign.html')

def listado_producto(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'core/listado_productos.html', data)

@permission_required('core.add_producto')
def nuevo_producto(request):
    data = {
        'form':ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
            data['form'] = formulario
    
    return render(request, 'core/nuevo_producto.html', data)
@permission_required('core.delete_producto','core.add_producto')
def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
        data['form'] = formulario
    return render(request, 'core/modificar_producto.html', data)
@permission_required('core.delete_producto','core.add_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    
    return redirect(to="listado_productos")

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, "registration/register.html", data)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



