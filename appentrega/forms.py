from django import forms

class formDatosPersonales(forms.Form):
    nombres = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=40)

class formPago(forms.Form):
    metodoPago = forms.CharField(max_length=30)
    cuotas = forms.IntegerField()

class formPrenda(forms.Form):
    nombre = forms.CharField(max_length=40)
    sexo = forms.CharField(max_length=1)
    talle = forms.CharField(max_length=4)
    color = forms.CharField(max_length=40)