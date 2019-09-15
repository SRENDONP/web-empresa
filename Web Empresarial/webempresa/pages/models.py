from django.db import models
from ckeditor.fields import RichTextField # esto es para poner un editor mas completo de texto en el administrador debo incluirlo en las apps del settings y cambiarlo en el tipo de campo para este caso en el campo content y siempre debo migrar los cambios

# Create your models here.

class Page (models.Model):
    title = models.CharField(verbose_name='Titulo',max_length=200)
    content = RichTextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='orden', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: # me permite visualizar el nombre en español y de igual manera me permite visualizarlo del mas reciente al mas antiguo
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["title"]

    def __str__(self):
        return self.title # esta funcion en el administrador me permite visualizar el nombre o titulo del proyecto que voy a modificar para identificarlo mas facilmentE