from django import forms, http
from .models import Categoria, Marca, Producto

from django.forms import ModelForm


class ProductoForm(forms.Form):
	nombre = forms.CharField(max_length=50)
	descripcion = forms.CharField(max_length=50)
	categoria = forms.ModelChoiceField(queryset= Categoria.objects.all())
	marca = forms.ModelChoiceField(queryset= Marca.objects.all())
	modelo = forms.CharField(max_length=50)
	foto = forms.ImageField()
	nro_serie = forms.IntegerField()
	stock = forms.IntegerField()
	costo = forms.IntegerField()
	precio_unitario = forms.IntegerField()

	class Meta:
		model = Producto
		exclude = ()


class CategoriaForm(forms.Form):
	nombre = forms.CharField(max_length=50)
	class Meta:
		model = Categoria
		exclude = ()


class MarcaForm(forms.Form):
	nombre = forms.CharField(max_length=50)
	class Meta:
		model = Marca
		exclude = ()
		

		