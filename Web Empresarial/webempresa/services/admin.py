from django.contrib import admin
from .models import service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin): # esta clase me permite visualizar en el administrador de proyectos los campos ocultos de created y updated pero no se pueden modificar 
    readonly_fields = ('created', 'updated')

admin.site.register(service, ServiceAdmin)# y es lo que me permite visualizar en el panel de administrador 