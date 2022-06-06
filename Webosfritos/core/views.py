import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import Receta

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login_view(request):
    return render(request, 'core/iniciarsesion.html')

def registro_view(request):
    return render(request, 'core/registrarse.html')

def recetas_view(request):
    return render(request, 'core/regis_recipe.html')

def crearReceta(request):
    titulo = request.POST.get('titulo', '')
    imagen = request.POST.get('imagen', '') 
    receta = request.POST.get('receta', '')
    user = request.user
    try:
        usuario = User.objects.get(pk=user.id)
        receta = Receta(titulo=titulo, imagen=imagen, parrafo=receta, usuario=usuario)
        receta.save()
        return redirect('crear_receta')
    except:
        context = {'error': 'No se pudo crear receta, debes tener tu sesion iniciada'}
        return render(request, 'core/regis_recipe.html', context=context)

def mostrar_mis_recetas(request):

    user = request.user
    
    try:
        usuario = User.objects.get(pk=user.id)
        recetas = Receta.objects.filter(usuario=usuario)
    except:
        recetas = False

    if user is None:
        user = 'Guest'

    context = {
        'recetas': recetas,
        'user': user
    }
    return render(request, 'core/mis_recetas.html', context=context)

def registrarUser(request):
    # DATOS TOMADOS ATRAVES DEL FORMULARIO
    nombre = request.POST.get('nombre','')
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    primernombre = request.POST.get('primernombre','')
    segundonombre = request.POST.get('segundonombre','')

    # CREACION DEL OBJETO
    try:
        user = User.objects.create_user(username = nombre, email = email, password = password, first_name = primernombre, last_name = segundonombre)
        user.save()
    except Exception:
        return redirect('registro_view')

    return redirect('home')


def iniciarSesion(request):
    password = request.POST.get('password', '')
    username = request.POST.get('username','')

    usuario = authenticate(request, username = username, password = password)

    if usuario is not None:
        auth_login(request, usuario)
        return redirect('home')
    else:
        return redirect('home')

def cerrarSesion(request):
    logout(request)
    return redirect('home')