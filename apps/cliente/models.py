from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	ci = models.IntegerField()
	telefono =models.IntegerField()
	direccion = models.CharField(max_length=200)
	
	def __unicode__(self):
	    return self.nombre	



