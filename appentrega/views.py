from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import *
from appentrega.forms import *
# Create your views here.

def inicio(request):
    return render(request, "appentrega/inicio.html")

def vdatosPersonales(request):
    if request.method == "POST":
        misDatosPersonales = formDatosPersonales(request.POST)
        print(misDatosPersonales)
        if misDatosPersonales.is_valid:
            informacion = misDatosPersonales.cleaned_data
            DP = datosPersonales(nombres=informacion["nombres"], apellido=informacion["apellido"], email=informacion["email"], telefono=informacion["telefono"])
            DP.save()
            return render(request, "appentrega/inicio.html")
    else:
        misDatosPersonales = formDatosPersonales()
    return render(request, "appentrega/datosPersonales.html", {"misDatosPersonales": misDatosPersonales})

def vprenda(request):
    if request.method == "POST":
        misprenda = formPrenda(request.POST)
        print(misprenda)
        if misprenda.is_valid:
            informacion = misprenda.cleaned_data
            PRENDA = prenda(nombre=informacion["nombre"], sexo=informacion["sexo"], talle=informacion["talle"], color=informacion["color"])
            PRENDA.save()
            return render(request, "appentrega/inicio.html")
    else:
        misprenda = formPrenda()
    return render(request, "appentrega/prenda.html", {"misprenda": misprenda})

def vpago(request):
    if request.method == "POST":
        misPago = formPago(request.POST)
        print(misPago)
        if misPago.is_valid:
            informacion = misPago.cleaned_data
            PAGO = pago(metodoPago=informacion["metodoPago"], cuotas=informacion["cuotas"])
            PAGO.save()
            return render(request, "appentrega/inicio.html")
    else:
        misPago = formPago()
    return render(request, "appentrega/pago.html", {"misPago": misPago})

def busquedaPrenda(request):
    return render(request, "appentrega/busquedaPrenda.html")

def buscar(request):
    if request.GET["nombres"]:
        nombre = request.GET['nombres']
        prendas = prenda.objects.filter(nombre__icontains=nombre)
        return render(request, "appentrega/resultadoPorBusqueda.html", {"nombres":nombre, "prendas":prendas})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)