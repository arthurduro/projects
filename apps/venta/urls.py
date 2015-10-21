from django.conf.urls import patterns, include, url
from .views import CrearProveedor, ListProveedor, EditView, DeleteProveedor

urlpatterns = patterns('',

    url(r'^CrearProveedor/$', CrearProveedor.as_view(), name='CrearProveedor'),
    # url(r'^listaProveedor/$', ListProveedor.as_view(), name='lista_proveedor'),
    # url(r'^edit_proveedor/(?P<pk>\d+)$', EditView.as_view(), name='proveedor_edit'),
    # url(r'^delete_proveedor/(?P<proveedor>\d+)$', 'apps.proveedor.views.DeleteProveedor', name='proveedor_delete'),

)