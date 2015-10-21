from django.db import models

# Create your models here.
class Proveedor(models.Model):
	nombre = models.CharField(max_length=50)
	ci = models.IntegerField()
	direccion = models.CharField(max_length=50)
	telefono = models.IntegerField()
	email = models.EmailField()
	url =	models.CharField(max_length=50)	
	
	def __unicode__(self):
	    return self.nombre




