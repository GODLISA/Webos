from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.index, name="home"),

    path('registro/', views.register, name="registro"),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/iniciarsesion.html'),
        name="mostrarInicio"
    ),

    path('crear_receta/', views.recetas_view, name='crear_receta'),
    path('crear_receta/go', views.crearReceta, name='crear'),

    path('mis_recetas/', views.mostrar_mis_recetas, name='mis_recetas'),
    path('receta/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('receta/edit/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('receta/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    # logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)