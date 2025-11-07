from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_hotel, name='inicio_hotel'),
    # URLs para CRUD de Categorías
    path('categorias/', views.ver_categorias, name='ver_categorias'),
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/actualizar/<int:id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categorias/borrar/<int:id>/', views.borrar_categoria, name='borrar_categoria'),
]