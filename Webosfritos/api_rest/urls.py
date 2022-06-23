from django.urls import path
from api_rest.views import listas_recetas,agregar_receta,modElimReceta, listas_usuario, agregar_usuario, modElimUsuario
from api_rest.viewsLogin import login
urlpatterns = [
    path('listas_recetas/',listas_recetas,name="listas_recetas"),
    path('agregar_receta/',agregar_receta,name="agregar_receta"),
    path('modElimReceta/<codigo>',modElimReceta,name="modElimReceta"),
    path('login/',login,name="login"),
    path('listas_usuario/',listas_usuario,name="listas_recetas"),
    path('agregar_usuario/',agregar_usuario,name="agregar_receta"),
    path('modElimUsuario/<codigo>',modElimUsuario,name="modElimReceta"),
]