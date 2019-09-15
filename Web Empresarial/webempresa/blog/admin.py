from django.contrib import admin
from .models import Category, post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin): # esta clase me permite visualizar en el administrador de proyectos los campos ocultos de created y updated pero no se pueden modificar 
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin): # esta clase me permite modificar el administrador de varias maneras para este caso estoy modificando las entradas 
    readonly_fields = ('created', 'updated')# este comando me permite tunear o personalizar los campos created y updated que sean de solo lectura
    list_display = ('title', 'author', 'published','post_categories') #aqui puedo visualizar estos campos en la lista del admin 
    ordering = ('author', 'published')# este comando me ordena los campos en la lista del administrador donde gestiono las entrdas
    search_fields = ('title', 'author__username')# este comando me pone una barra de busqueda en el administrador para buscar porlos campos que le indique dentro de la tupla   
    date_hierarchy = 'published' # este me muestra por orden de jerarquia la fecha aninada por año mes ...
    list_filter = ('author__username', 'categories__name')# este comando me muesta del lado derecho una serie de filtros en este caso por author
    list_per_page = 10 # este me muestra el numero de entradas por paginas

    def post_categories(self, obj): # este metodo me permite mostrar en la lista las categories que se encuentran en un manytomany
        return ', '.join([c.name for c in obj.categories.all().order_by('name')]) 

admin.site.register(Category, CategoryAdmin)# y es lo que me permite visualizar en el panel de administrador 

admin.site.register(post, PostAdmin)# y es lo que me permite visualizar en el panel de administrador 