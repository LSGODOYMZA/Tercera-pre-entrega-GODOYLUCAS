from django.contrib import admin
from .models import Categoria, Clubes, Usuario

# Register your models here.

admin.site.register (Clubes)
admin.site.register (Usuario)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Equipos', 'clubes_asociados')

admin.site.register(Categoria, CategoriaAdmin)