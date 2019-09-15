from django.shortcuts import render, redirect # el redirect me permite despues de enviar el formulario redireccionar a una pagina
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm (data=request.POST) # este if me esta pintando los elementos que envie por el fomulario osea que cuando le doy enviar la pagina no me limpia los campos sino que me los con al informaicon que envie 
        if contact_form.is_valid(): 
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                    "la caffettiera nuevo mensaje de contacto", #asunto,
                    "de {} <{}>\n\nEscribio:\n\n{}".format(name, email, content), #cuerpo,
                    "no-contestar@inbox.mailtrap.io", #email_origen,
                    ["rendonsebastian95@gmail.com"], #email_destino,
                    reply_to=[email]
            )
            try: #con el try prueba que si envie, si no envia se desvia por el except
                email.send()
                return redirect (reverse('contact')+"?Ok") # todo ha salido perfecto entonces me pone ok en la url
            except:
                    # algo a salido mal y redirect entonces me pone fail en el url
                return redirect (reverse('contact')+"?fail")# aqui es como un template tag pero de url para que el me gestione automaticamente donde me debe llevar luego de que envio un correo y me pone el ?ok en la url

    return render(request, 'contact/contact.html', {'form': contact_form})
