from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Solicitud

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
from .serializer import SolicitudSerializer

#CRUD USUARIOS
def crear_U(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    direccion = request.POST.get('direccion')
    ciudad = request.POST.get('ciudad')
    comuna = request.POST.get('comuna')
    usuario = Usuario(username=username,email=email,password=password,direccion=direccion,
    ciudad=ciudad,comuna=comuna)
    usu =User(username=username,email=email,password=password)
    usuario.save()
    usu.save()
    return redirect('index')
    


#CRUD PRODUCTOS




#CRUD SOLICITUDES
def soli_t(request):
    nombres = request.POST.get('nombres')
    email = request.POST.get('email')
    asunto = request.POST.get('asunto')
    mensaje = request.POST.get('mensaje')
    solicitud = Solicitud(nombres=nombres,email=email,asunto=asunto,mensaje=mensaje)
    solicitud.save()
    return redirect ('index')




#Serialyzer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer