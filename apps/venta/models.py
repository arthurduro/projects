from django.db import models
from apps.cliente.models import Cliente

# Create your models here.
class Venta(models.Model):
	cliente = models.ForeignKey(Cliente)
	total_venta = models.IntegerField()
	
		