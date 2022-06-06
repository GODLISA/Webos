from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from Webosfritos import settings

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre usuario')
    apellido = models.CharField(max_length=34, null=False, verbose_name='Apellido usuairo')
    mail = models.CharField(max_length=60,null=False, verbose_name='email del usuario')
    contrasena = models.CharField(max_length=16, null=False, verbose_name='contrasena de usuario')

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    idreceta = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20, null=False, verbose_name='Titulo de la receta')
    imagen = models.ImageField(upload_to='recetas', null= True)
    parrafo = models.CharField(max_length=1200, null=False, verbose_name='Descripcion de la receta')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.titulo, self.usuario)