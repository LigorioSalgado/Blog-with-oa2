from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Index(request):
    user = request.user

    return render(request,'Home/index.html',{"user":user})


def Contacto(request):

    return HttpResponse('Pagina de contactos')

def Otros(request,num,num2):

    return HttpResponse('Pagina de otros numero: <b> '+num+'</b>')

def Signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is  None:
            user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password)
            user.save()
            return HttpResponse('<b>Usuario Registrado<b>')
        else:
            return HttpResponse('<b>El usuario que ingresaste ya existe<b>')


    else:
        return render(request,'Home/signup.html')

def Login(request):

    if request.method == 'POST':

        user = authenticate(username=request.POST['username'],
        password=request.POST['password'])

        if user is not None:
            login(request,user)
            return redirect('Home:index')

        else:
            return HttpResponse("Error en usuario o contraseña")

    else:
        return render(request,'Home/login.html')


def Logout(request):
    logout(request)
    return redirect('Home:index')
