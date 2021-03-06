from distutils.log import Log
from pickletools import read_uint1
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView)
from .models import Receta
from .forms import UserRegisterForm
from django.contrib import messages
from Webosfritos.settings import BASE_DIR

# Create your views here.

def index(request):
    user = request.user

    try:
        recetas = Receta.objects.all()
    except:
        recetas = ''

    if user is None:
        user = 'Guest'

    context = {
        'recetas': recetas,
        'user': user
    }
    return render(request, 'core/index.html', context)

def login_view(request):
    return render(request, 'core/iniciarsesion.html')

def recetas_view(request):

    if request.user.is_authenticated:
        return render(request, 'core/regis_recipe.html')
    else:
        return redirect('registro')

def crearReceta(request):
    titulo = request.POST.get('titulo', '')
    imagen = request.FILES.get('imagen', '') 
    receta = request.POST.get('receta', '')
    user = request.user

    try:
        usuario = User.objects.get(pk=user.id)
        receta = Receta(titulo=titulo, imagen=imagen, parrafo=receta, usuario=usuario)
        receta.save()
        return redirect('register')
    except:
        context = {'error': 'No se pudo crear receta, debes tener tu sesion iniciada'}
        return render(request, 'core/regis_recipe.html', context=context)

def mostrar_mis_recetas(request):

    user = request.user

    try:
        usuario = User.objects.get(pk=user.id)

        if usuario.is_staff:
            recetas = Receta.objects.all()
        else:
            recetas = Receta.objects.filter(usuario=usuario).order_by('-idreceta')
    except:
        recetas = ''

    if user is None:
        user = 'Guest'

    context = {
        'recetas': recetas,
        'user': user
    }
    return render(request, 'core/my_post.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Felicidades {username}, ahora eres uno de nosotros!')
            return redirect('home')
        else:

            return render(request, 'core/registrarse.html', {"Mensaje": True, 'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'core/registrarse.html', {'form': form})


class PostDetailView(DetailView):
    model = Receta

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Receta
    fields = ['titulo', 'imagen', 'parrafo']

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Receta
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

