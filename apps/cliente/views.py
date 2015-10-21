from django.shortcuts import render
from .forms import ClienteForm
from django.views.generic import CreateView,FormView, ListView, UpdateView, DeleteView, DetailView
from .models import Cliente
from pure_pagination.mixins import PaginationMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

# Create your views here.
class CrearCliente(FormView):
	template_name = 'cliente/create.html'
	form_class = ClienteForm
	success_url = reverse_lazy('lista_cliente')

	def form_valid(self, form):
		cliente = Cliente()
		cliente.nombre = form.cleaned_data['nombre']
		cliente.apellido = form.cleaned_data['apellido']
		cliente.ci = form.cleaned_data['ci']
		cliente.telefono = form.cleaned_data['telefono']
		cliente.direccion = form.cleaned_data['direccion']
		cliente.save()
		return super(CrearCliente, self).form_valid(form)



class ListCliente(PaginationMixin, ListView):
	template_name = "cliente/lista.html"
	model = Cliente
	paginate_by = 2
	queryset = Cliente.objects.all().order_by('pk')


class EditView(SuccessMessageMixin, UpdateView):
	template_name = 'cliente/update.html'
	model = Cliente
	success_url = reverse_lazy('lista_cliente')
	fields =['nombre','apellido','ci','telefono','direccion']
	success_message = "%(nombre)s was created successfully"


def DeleteCliente(request,cliente):
	e = Cliente.objects.get(id=cliente)
	e.delete()
	print e
	return HttpResponseRedirect(reverse_lazy('lista_cliente'))

