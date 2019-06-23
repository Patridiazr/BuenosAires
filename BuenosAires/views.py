from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Create your views here.
def index(request):
    return render(request,'index.html')
def navbar(request):
    return render(request,'navbar.html')
def footer (request):
    return render (request,'footer.html')
def productos (request):
    return render (request,'productos.html')
def solicitud (request):
    return render (request,'solicitud.html')

#import de api
from rest_framework import viewsets
from .serializer import UsuarioSerializer

#CRUD USUARIOS
def crear_U(request):
    rut = request.POST.get('rut','')
    nombre = request.POST.get('nombre','')
    apellido = request.POST.get('apellido','')
    email = request.POST.get('email','')
    contraseña = request.POST.get('contraseña','')
    direccion = request.POST.get('direccion','')
    ciudad = request.POST.get('ciudad','')
    comuna = request.POST.get('comuna','')
    codpos = request.POST.get('codpos','')
    usuario = Usuario(rut=rut,nombre=nombre, apellido=apellido,email=email,contraseña=contraseña,direccion=direccion,ciudad=ciudad,
    comuna=comuna,codpos=codpos)
    usu =User(rut=rut,nombre=nombre, apellido=apellido,email=email,contraseña=contraseña,direccion=direccion,ciudad=ciudad,
    comuna=comuna,codpos=codpos)
    usuario.save()
    usu.save()
    return redirect('solicitud')



#CRUD PRODUCTOS




#CRUD SOLICITUDES


#Serialyzer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer