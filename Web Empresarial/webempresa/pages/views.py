from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def page (request, page_id): # defino el metodo
    page = get_object_or_404 (Page, id =page_id) # esta variable me busca por id y si no lo encuentra me retorna a error 404
    return render (request,'pages/sample.html',{'page': page})