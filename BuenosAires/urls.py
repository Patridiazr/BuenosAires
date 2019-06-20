from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path('',views.navbar,name="navbar"),
   path('',views.footer,name="footer"),
   path('productos',views.productos,name="productos"),
   path('solicitud',views.solicitud,name="solicitud")
]
