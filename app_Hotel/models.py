from django.db import models

# Create your models here.
# ==========================================
# MODELO: EMPLEADOS
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    fecha_contratacion = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"

# ==========================================

# MODELO: HUÉSPEDES
# ==========================================
class Huesped(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: HABITACIONES
# ==========================================
class Habitacion(models.Model):
    numero_habitacion = models.PositiveIntegerField(unique=True)
    tipo = models.CharField(max_length=50)
    precio_noche = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)
    huesped = models.ForeignKey(Huesped, on_delete=models.SET_NULL, null=True, blank=True, related_name="habitaciones")

    def __str__(self):
        return f"Habitación {self.numero_habitacion} - {self.tipo}"

# ==========================================
# MODELO: CATEGORÍA (Para Cinépolis, interpretando la instrucción 27)
# ==========================================
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre