from django.shortcuts import render
from django.views.generic import ListView 
from .models import Compra 
from pure_pagination.mixins import PaginationMixin

class ListCompra(PaginationMixin, ListView):
	template_name = "compra/Lista.html"
	model = Compra	
	queryset = Compra.objects.all().order_by('pk')	