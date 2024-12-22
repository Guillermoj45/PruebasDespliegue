from django.http import HttpResponse
from django.shortcuts import render

from pruebasPruebas.models import Usuario
from django.http import JsonResponse

# Create your views here.


def home(request):
    usuarios = list(Usuario.objects.values())
    return JsonResponse({'usuarios': usuarios})

