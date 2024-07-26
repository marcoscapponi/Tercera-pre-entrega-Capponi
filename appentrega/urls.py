from django.urls import path
from appentrega.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('datospersonales', vdatosPersonales, name="datosPersonales"),
    path('pago', vpago, name="pago"),
    path('prenda', vprenda, name="prenda"),
    path('busquedaPrenda', busquedaPrenda, name="BusquedaCamada"),
    path('buscar/', buscar)
]