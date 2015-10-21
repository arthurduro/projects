from django.db import models
from apps.proveedor.models import Proveedor  
from apps.producto.models import Producto  

# Create your models here.
class Compra(models.Model):
	fecha = models.DateField()
	proveedor = models.ForeignKey(Proveedor)
	tipo_pago = models.CharField(max_length=100)
	producto = models.ForeignKey(Producto)
	
    

								