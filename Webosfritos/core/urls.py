from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="home"),
        # INICIO

    # REGISTRO
    path('registro', views.registro_view, name="mostrarRegistro"),
    path('registro/registrar', views.registrarUser, name="registrarUser"),

    # LOGIN

    path('login/', views.login_view, name="mostrarInicio"),
    path('login/iniciarSesion', views.iniciarSesion, name="iniciarSesion"),

    #Recetas
    
    path('crear_receta/', views.recetas_view, name='crear_receta'),
    path('crear_receta/go', views.crearReceta, name='crear'),
    path('mis_recetas/', views.mostrar_mis_recetas, name='mis_recetas'),

    # logout
    path('logout/', views.logout, name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)