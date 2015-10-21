from django import forms, http
from .models import Cliente

from django.forms import ModelForm

class ClienteForm(forms.Form):
	nombre = forms.CharField(max_length=50)
	apellido = forms.CharField(max_length=50)
	ci = forms.IntegerField()
	telefono = forms.IntegerField()
	direccion = forms.CharField(max_length=50)
	class Meta:
		model = Cliente