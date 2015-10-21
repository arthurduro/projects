from django.conf.urls import patterns, include, url
from .views import ListCompra 


urlpatterns = patterns('',

   url(r'^ListaCompra/', ListCompra.as_view(), name='lista_compra'),
)