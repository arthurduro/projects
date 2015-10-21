from django.conf.urls import patterns, include, url
from .views import ListCliente, EditView, CrearCliente, DeleteCliente


urlpatterns = patterns('',

	url(r'^Createcliente/', CrearCliente.as_view(), name='CrearCliente'),
    url(r'^listacliente/', ListCliente.as_view(), name='lista_cliente'),
    url(r'^edit_cliente/(?P<pk>\d+)$', EditView.as_view(), name='cliente_edit'),
    url(r'^delete_cliente/(?P<cliente>\d+)$', 'apps.cliente.views.DeleteCliente', name='cliente_delete'),

)

