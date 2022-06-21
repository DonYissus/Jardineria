from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):
    
    nombre = forms.CharField(min_length=2, max_length=50)
    cantidad = forms.IntegerField(min_value=1, max_value=100)
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad', 'TipoProducto', 'DetalleProducto']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
