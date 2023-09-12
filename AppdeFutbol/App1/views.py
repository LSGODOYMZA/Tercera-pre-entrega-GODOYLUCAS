from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from .forms import UsuarioFormulario, ClubesFormulario

# Create your views here.

def inicio (req):
    
    return render (req, "Inicio.html")

def crear_usuario (req):
    if req.method == 'POST':
        mi_formulario = UsuarioFormulario (req.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            usuario = Usuario (Nombre=data['nombre'], Email=data['email'],Hincha=data['hincha'], Contraseña=data['contraseña'])
            usuario.save()
            return HttpResponse (f'{usuario.Nombre_Usuario} hincha de {usuario.Hincha} creado exitosamente')
        pass
    else:
        mi_formulario = UsuarioFormulario ()
        return render (req, "usuario_formularios.html", {'mi_formulario': mi_formulario})


def crear_equipos (request):
    if request.method == 'POST':
        nombre = request.POST.get('Nombre')
        ciudad = request.POST.get('Ciudad')
        provincia = request.POST.get('Provincia')
        categoria_nombre = request.POST.get('Categoria')
        print(f'categoria_nombre recibida del formulario: {categoria_nombre}')
        try:
         categoria = Categoria.objects.get(Nombre=categoria_nombre)
        except Categoria.DoesNotExist:
            return HttpResponse('La categoría ingresada no existe.')
        club_existente = Clubes.objects.filter(Nombre=nombre, Ciudad=ciudad, Provincia=provincia).first()
        
        if club_existente:
            return HttpResponse(f'El club "{nombre}" ya existe en la misma localidad.')
        equipo = Clubes(Nombre=nombre, Ciudad=ciudad, Provincia=provincia, Categoria=categoria)
        equipo.save()
        return HttpResponse (f'{equipo.Nombre} creado exitosamente')
    else:
        mi_formulario = ClubesFormulario ()
        return render (request, "clubes_formularios.html", {'mi_formulario': mi_formulario})
def busqueda_equipos(req):
    
    return render (req, 'BusquedaEquipos.html')

def buscar_equipos(req):
    query = req.GET.get('q')
    if query:
        resultados = Clubes.objects.filter(Nombre=query)
    else:
        resultados = Clubes.objects.all()
    
    return render(req, 'ResultadoBusqueda.html', {'resultados': resultados})


def categorias(req):
    
    lista = Categoria.objects.all()
    
    return render (req, "Categorias.html", {"Categorias":lista})

def equipos(req):
    
    equipos = Clubes.objects.all().order_by('Categoria__Nombre', 'Nombre', 'Ciudad')
    return render(req, 'Equipos.html', {'equipos': equipos})


