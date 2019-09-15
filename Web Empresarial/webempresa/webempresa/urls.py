"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views #aqui hago la importacion de mis vistas creadas en core
from django.conf import settings

urlpatterns = [
    #path del core importacion
    path('', include('core.urls')),

    #path del services importacion
    path('services/', include('services.urls')),

    #path del blog
    #path('', include('blog.urls')),
    path('blog/', include('blog.urls')),
    
    #path del page
    path('page/', include('pages.urls')),

    #path del contact
    path('contact/', include('contact.urls')),

    #path del admin
    path('admin/', admin.site.urls),


]


# metodo que me permite visualizar las imagenes cuando estoy en entorno de desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # SOLO DE ESTA MANERA PUEDO VER LAS IMAGENES QUE SUBA A CADA PROYECTO CREADO DESDE EL ADMINISTRADOR
