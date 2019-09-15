from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required = True, widget = forms.TextInput(
        attrs={'class':'form-control'} # el widget me permite darle estilo al campo que se muestra en el template, extendiendo la configuracion
    ), min_length=4, max_length=100)# el min y max_length es para que me valide el numero de caracteres que deben ir en el campo input
    email = forms.EmailField(label = 'Email', required = True, widget = forms.EmailInput(
        attrs={'class':'form-control'} # el widget me permite darle estilo al campo que se muestra en el template, extendiendo la configuracion
    ), min_length=4, max_length=100)
    content = forms.CharField(label = 'Contenido', required = True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Dejanos Tu Mensaje Aqui'} # el widget me permite darle estilo al campo que se muestra en el template, extendiendo la configuracion, el row 3 es para que me muestre en el template solo 3 lineas se puede modificar y el place holder es para poner un mensaje de indicio en el campo
    ), min_length=4, max_length=500)
