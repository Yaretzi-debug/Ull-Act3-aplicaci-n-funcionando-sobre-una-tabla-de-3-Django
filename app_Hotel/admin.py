from django.contrib import admin
from .models import Empleado, Huesped, Habitacion, Categoria

# Registra tus modelos aquí.
admin.site.register(Empleado)
admin.site.register(Huesped)
admin.site.register(Habitacion)
admin.site.register(Categoria)