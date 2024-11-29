from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Hola, este es mi proyecto Django llamado my_site!")


# Create your views here.
