from django import forms, http
from django.forms import ModelForm
from .models import Proveedor


		
class ProveedorForm(forms.Form):
	nombre =  forms.CharField(max_length=50)
	ci = forms.IntegerField()
	direccion = forms.CharField(max_length=50)
	telefono = forms.IntegerField()
	email = forms.EmailField()
	url = forms.CharField(max_length=50)	

	class Meta:
		model = Proveedor
    
