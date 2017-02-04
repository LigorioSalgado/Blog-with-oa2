from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Index(request):

    return render(request,'Home/index.html')


def Contacto(request):

    return HttpResponse('Pagina de contactos')

def Otros(request,num,num2):

    return HttpResponse('Pagina de otros numero: <b> '+num+'</b>')
