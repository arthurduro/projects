from django.contrib import admin
from .models import Compra, Detalle_compra


# Register your models here.
django.site.register(Compra)
django.site.register(Detalle_compra)
