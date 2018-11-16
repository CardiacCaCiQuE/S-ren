from django.shortcuts import render

# Create your views here.
def ListaPerros(request):
    return render(request,"ListaPerros.html")

def AgregarPerros(request):
    return render(request,"CrearPerros.html")