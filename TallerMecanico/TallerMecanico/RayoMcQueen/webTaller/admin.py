from django.contrib import admin
from .models import Categoria,Reparacion,Galeria,Repuesto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Reparacion)
admin.site.register(Galeria)
admin.site.register(Repuesto)