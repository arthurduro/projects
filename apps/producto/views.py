from django.shortcuts import render
from django.views.generic import CreateView,FormView, ListView, UpdateView, DeleteView, DetailView
from .models import Producto
from pure_pagination.mixins import PaginationMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class ListProducto(PaginationMixin, ListView):
	template_name = "producto/lista.html"
	model = Producto
	paginate_by = 2
	queryset = Producto.objects.all().order_by('pk')


class EditView(SuccessMessageMixin, UpdateView):
    template_name = 'producto/update.html'
    model = Producto
    success_url = reverse_lazy('lista')
    fields = ['nombre','descripcion','categoria','marca','modelo','foto','nro_serie','stock','costo','precio_unitario']
    success_message = "%(nombre)s was created successfully"