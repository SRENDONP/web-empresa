from django.shortcuts import render
from .models import service # esta importacion me hace referencia al modelo service

# Create your views here.

def services(request):
    services = service.objects.all()# aqui creo una variable que me contiene todos los elementos de la tabla o clase service del modelo, y el .all es para que me traiga todos los elementos
    return render(request, 'services/services.html',{'services': services})# los envia con un diccionario de contexto con la clave services y le paso la variable que cree arriba
