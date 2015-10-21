from django.shortcuts import render
from .forms import ProductoForm, CategoriaForm, MarcaForm
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView, DetailView
from .models import Producto, Categoria, Marca
from pure_pagination.mixins import PaginationMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect



# Create your views here. categoria
class CrearCategoria(FormView):
	template_name = 'categoria/create.html'
	model = Categoria
	form_class = CategoriaForm
	success_url = reverse_lazy('lista_categoria')

	def form_valid(self, form):
		categoria = Categoria()
		categoria.nombre = form.cleaned_data['nombre']
		categoria.save()
		return super(CrearCategoria, self).form_valid(form)


class ListCategoria(PaginationMixin, ListView):
	template_name = "categoria/lista.html"
	model = Categoria
	paginate_by = 2
	queryset = Categoria.objects.all().order_by('pk')


class EditCategoria(SuccessMessageMixin, UpdateView):
    template_name = 'categoria/update.html'
    model = Categoria
    success_url = reverse_lazy('lista_categoria')
    fields = ['nombre']
    success_message = "%(nombre)s was created successfully"


def DeleteCategoria(request, categoria):
	e = Categoria.objects.get(id=categoria)
	e.delete()
	print e
	return HttpResponseRedirect(reverse_lazy('lista_categoria'))


# Create your views here. marca
class CrearMarca(FormView):
	template_name = 'marca/create.html'
	model = Marca
	form_class = MarcaForm
	success_url = reverse_lazy('lista_marca')

	def form_valid(self, form):
		marca = Marca()
		marca.nombre = form.cleaned_data['nombre']
		marca.save()
		return super(CrearMarca, self).form_valid(form)


class ListMarca(PaginationMixin, ListView):
	template_name = "marca/lista.html"
	model =  Marca
	paginate_by = 2
	queryset = Marca.objects.all().order_by('pk')

class EditMarca(SuccessMessageMixin, UpdateView):
    template_name = 'marca/update.html'
    model = Marca
    success_url = reverse_lazy('lista_marca')
    fields = ['nombre']
    success_message = "%(nombre)s was created successfully"


def DeleteMarca(request,marca):
	e = Marca.objects.get(id=marca)
	e.delete()
	print e
	return HttpResponseRedirect(reverse_lazy('lista_marca'))



# Create your views here. producto		
class CrearProducto(FormView):
	template_name = 'producto/create.html'
	form_class = ProductoForm
	success_url = reverse_lazy('lista_producto')

	def form_valid(self, form):
		producto = Producto()
		producto.nombre = form.cleaned_data['nombre']
		producto.descripcion = form.cleaned_data['descripcion']
		producto.categoria = form.cleaned_data['categoria']
		producto.marca = form.cleaned_data['marca']
		producto.modelo = form.cleaned_data['modelo']
		producto.foto = form.cleaned_data['foto']	
		producto.nro_serie = form.cleaned_data['nro_serie']
		producto.stock = form.cleaned_data['stock']
		producto.costo = form.cleaned_data['costo']
		producto.precio_unitario = form.cleaned_data['precio_unitario']
		producto.save()
		return super(CrearProducto, self).form_valid(form)


class ListProducto(PaginationMixin, ListView):
	template_name = "producto/lista.html"
	model = Producto
	paginate_by = 2
	queryset = Producto.objects.all().order_by('pk')


class EditProducto(SuccessMessageMixin, UpdateView):
    template_name = 'producto/update.html'
    model = Producto
    success_url = reverse_lazy('lista_producto')
    fields = ['nombre','descripcion','categoria','marca','modelo','foto','nro_serie','stock','costo','precio_unitario']
    success_message = "%(nombre)s was created successfully"


def DeleteProducto(request,producto):
	e = Producto.objects.get(id=producto)
	e.delete()
	print e
	return HttpResponseRedirect(reverse_lazy('lista_producto'))    