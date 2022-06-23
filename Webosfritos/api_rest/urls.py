from django.urls import path
from api_rest.views import listas_mascotas,agregar_mascota,modElimMascota
from api_rest.viewsLogin import login
urlpatterns = [
    path('listas_mascotas/',listas_mascotas,name="listas_mascotas"),
    path('agregar_mascota/',agregar_mascota,name="agregar_mascota"),
    path('modElimMascota/<codigo>',modElimMascota,name="modElimMascota"),
    path('login/',login,name="login"),
]