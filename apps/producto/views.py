from django.shortcuts import render
from django.views.generic import CreateView,FormView, ListView, UpdateView, DeleteView, DetailView
from .models import Producto
# Create your views here.
class ListProducto(ListView):
	template_name = "producto/lista.html"
	model = Producto
	queryset = Producto.objects.all().order_by('pk')