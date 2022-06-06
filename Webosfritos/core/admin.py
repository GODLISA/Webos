from django.contrib import admin
from core.models import Usuario, Receta
# Register your models here.



"""
class EconomicActivityAdmin(admin.ModelAdmin):

    model = EconomicActivity

    search_fields = ('name__unaccent', 'code')

    list_display = ('name', 'code', 'iva', 'tribute', 'net')

    list_filter = (
        'iva',
        'tribute',
        'net',
)
"""
admin.site.register(Usuario)
admin.site.register(Receta)

class UsuariosAdmin(admin.ModelAdmin):
    model = Usuario
    search_fields = ('nombre__unaccent', 'apellido__unaccent')
    list_display = ('nombre', 'apellido')

class Receta(admin.ModelAdmin):
    model = Receta