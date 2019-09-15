from django.db import models

# Create your models here.

class service(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    subtitle = models.CharField(max_length=200, verbose_name = "Subtitulo")
    image = models.ImageField(verbose_name = "Imagen", upload_to= "services")
    content = models.TextField(verbose_name = "Contenido")
    #link = models.URLField(verbose_name = "Direccion Web",null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: # me permite visualizar el nombre en español y de igual manera me permite visualizarlo del mas reciente al mas antiguo
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.title # esta funcion en el administrador me permite visualizar el nombre o titulo del proyecto que voy a modificar para identificarlo mas facilmentE