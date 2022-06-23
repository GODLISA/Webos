from django.urls import path
from api_rest.views import listas_recetas,agregar_receta,modElimReceta
from api_rest.viewsLogin import login
urlpatterns = [
    path('listas_recetas/',listas_recetas,name="listas_recetas"),
    path('agregar_receta/',agregar_receta,name="agregar_receta"),
    path('modElimReceta/<codigo>',modElimReceta,name="modElimReceta"),
    path('login/',login,name="login"),
]