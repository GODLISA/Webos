from pickletools import read_uint1
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_login
from .models import Receta
from .forms import UserRegisterForm
from django.contrib import messages
from Webosfritos.settings import BASE_DIR
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login_view(request):
    return render(request, 'core/iniciarsesion.html')

def recetas_view(request):
    print(Receta.objects.all())
    return render(request, 'core/regis_recipe.html')

def crearReceta(request):
    titulo = request.POST.get('titulo', '')
    imagen = request.FILES.get('imagen', '') 
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
        print("usuario %s" % usuario.is_staff)
        if usuario.is_staff:
            recetas = Receta.objects.all()
        else:
            recetas = Receta.objects.filter(usuario=usuario)
    except:
        recetas = ''

    if user is None:
        user = 'Guest'

    context = {
        'recetas': recetas,
        'user': user
    }
    return render(request, 'core/mis_recetas.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Felicidades {username}, ahora eres uno de nosotros!')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'core/registrarse.html', {'form': form})
