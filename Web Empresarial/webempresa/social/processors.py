# esto debo añadirlo al settings.py para que me funcione sin problemas 'social.processors.ctx_dict'

from .models import Link

def ctx_dict(request):
    ctx = {} # este dicccionario
    links = Link.objects.all()
    for link in links: # ESTE FOR ES PARA QUE ME BUSQUE EN LA BASE DE DATOS O EN EL MODELO LINK LAS REDES SOCIALES QUE TENGO PARA LUEGO INYECTARLAS EN EL HTML BASE
        ctx[link.key] = link.url
    return ctx