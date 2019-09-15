from django.shortcuts import render, HttpResponse


# Create your views here, aqui creo las vistas de todos mis modulos o pantallas

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')



