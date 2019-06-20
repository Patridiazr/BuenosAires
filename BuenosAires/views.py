from django.shortcuts import render

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

#CRUD USUARIOS




#CRUD PRODUCTOS




#CRUD SOLICITUDES