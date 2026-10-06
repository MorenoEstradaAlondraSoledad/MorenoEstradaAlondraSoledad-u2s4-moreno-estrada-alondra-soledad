from django.contrib import admin
from .models import Servicio, Inicio  # Asegúrate de poner los nombres exactos de tus modelos en models.py

admin.site.register(Servicio)
admin.site.register(Inicio)

# Register your models here.
