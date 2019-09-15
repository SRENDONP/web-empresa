from django.db import models

# Create your models here.

class Link (models.Model):
    key = models.SlugField(verbose_name='Nombre clave',max_length=100, unique= True )
    name = models.CharField(verbose_name='Red Social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: # me permite visualizar el nombre en español y de igual manera me permite visualizarlo del mas reciente al mas antiguo
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]

    def __str__(self):
        return self.name # esta funcion en el administrador me permite visualizar el nombre o titulo del proyecto que voy a modificar para identificarlo mas facilmentE