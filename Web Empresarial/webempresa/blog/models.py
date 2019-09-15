from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=100, verbose_name ='Categoria')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: # me permite visualizar el nombre en español y de igual manera me permite visualizarlo del mas reciente al mas antiguo
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name # esta funcion en el administrador me permite visualizar el nombre o titulo del proyecto que voy a modificar para identificarlo mas facilmente

class post(models.Model):
    title= models.CharField(max_length=200, verbose_name ='Titulo')
    content= models.TextField(verbose_name='Contenido')
    published= models.DateTimeField(verbose_name='Fecha de Publicacion', default=now)
    image= models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author= models.ForeignKey(User, verbose_name= 'Autor', on_delete=models.CASCADE)# de esta forma creo una llave foranea en este caso con la tabla de usuarios de django
    categories= models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: # me permite visualizar el nombre en español y de igual manera me permite visualizarlo del mas reciente al mas antiguo
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title # esta funcion en el administrador me permite visualizar el nombre o titulo del proyecto que voy a modificar para identificarlo mas facilmente