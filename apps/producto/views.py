from django.shortcuts import render
from django.views.generic import CreateView,FormView, ListView, UpdateView, DeleteView, DetailView
from .models import Producto
from pure_pagination.mixins import PaginationMixin
# Create your views here.
class ListProducto(PaginationMixin, ListView):
	template_name = "producto/lista.html"
	model = Producto
	paginate_by = 1
	queryset = Producto.objects.all().order_by('pk')