from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path('',views.navbar,name="navbar"),
   path('',views.footer,name="footer"),
   path('',views.productos,name="productos")
]
