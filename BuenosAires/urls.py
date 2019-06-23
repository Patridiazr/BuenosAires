from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)

urlpatterns = [
   #NAVEGACION PAGINA
   path('',views.index,name="index"),
   path('',views.navbar,name="navbar"),
   path('',views.footer,name="footer"),
   path('productos',views.productos,name="productos"),
   path('solicitud',views.solicitud,name="solicitud"),


   #CRUD USUARIOS
   path('navbar/needs-validation/crear_U',views.crear_U, name="crear_U"),

   path('productos',views.productos,name="productos"),
   path('solicitud',views.solicitud,name="solicitud"),
   

   #API'S
   path('api/', include(router.urls)), 
]
