from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView, FormView, UpdateView, DeleteView
from .models import Proveedor
from django.core.urlresolvers import reverse_lazy 
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

from .forms import ProveedorForm

# Create your views here.
class CrearProveedor(FormView):
	template_name='proveedor/crear.html'
	form_class = ProveedorForm
	success_url = reverse_lazy('lista_proveedor')

	def form_valid(self, form):
		proveedor = Proveedor()
		proveedor.nombre = form.cleaned_data['nombre']
		proveedor.ci = form.cleaned_data['ci']
		proveedor.direccion = form.cleaned_data['direccion']
		proveedor.telefono = form.cleaned_data['telefono']
		proveedor.email = form.cleaned_data['email']
		proveedor.url = form.cleaned_data['url']	
		proveedor.save()
		return super(CrearProveedor, self).form_valid(form)

class ListProveedor(ListView):
	template_name='proveedor/lista.html'
	model = Proveedor
	queryset = Proveedor.objects.all().order_by('pk')

class EditView(SuccessMessageMixin, UpdateView):
	template_name = 'proveedor/update.html'
	model = Proveedor
	success_url = reverse_lazy('lista_proveedor')
	fields = ['nombre','ci','direccion','telefono','email','url']
	success_message = "%(nombre)s was created successfully"


def DeleteProveedor(request,proveedor):
	e = Proveedor.objects.get(id=proveedor)
	e.delete()
	print e
	return HttpResponseRedirect(reverse_lazy('lista_proveedor'))
