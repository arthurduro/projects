from django.db import models

# Create your models here.

class Marca(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
	    return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)	
	def __unicode__(self):
	    return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria)
	marca = models.ForeignKey(Marca)
	modelo = models.CharField(max_length=100)
	foto = models.ImageField(upload_to='productos')
	nro_serie = models.IntegerField()
	stock = models.IntegerField()	
	costo = models.IntegerField()
	precio_unitario = models.IntegerField()

	def __unicode__(self):
	    return self.nombre

class Almacen(models.Model):
	nombre = models.CharField(max_length=100)
	producto =models.ForeignKey(Producto)

		


	
		
