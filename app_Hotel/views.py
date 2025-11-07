from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria # Importamos solo Categoria por ahora

# Función de inicio del Hotel
def inicio_hotel(request):
    return render(request, 'app_Hotel/inicio.html')

# ==========================================
# FUNCIONES CRUD PARA CATEGORÍAS
# ==========================================

def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        Categoria.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('ver_categorias')
    return render(request, 'app_Hotel/categoria/agregar_categoria.html')

def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'app_Hotel/categoria/ver_categorias.html', {'categorias': categorias})

def actualizar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.save()
        return redirect('ver_categorias')
    return render(request, 'app_Hotel/categoria/actualizar_categoria.html', {'categoria': categoria})

def borrar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST': # Confirmación de borrado
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'app_Hotel/categoria/borrar_categoria.html', {'categoria': categoria})

# (Las funciones para Huespedes y Habitaciones se dejarán pendientes)
