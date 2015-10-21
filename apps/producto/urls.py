from django.conf.urls import patterns, include, url
from .views import ListProducto, EditProducto, CrearProducto, DeleteProducto, CrearCategoria, ListCategoria, EditCategoria, DeleteCategoria, CrearMarca, ListMarca, EditMarca, DeleteMarca


urlpatterns = patterns('',

	url(r'^Createproducto/', CrearProducto.as_view(), name='CrearProducto'),
    url(r'^listaproducto/', ListProducto.as_view(), name='lista_producto'),
    url(r'^edit_producto/(?P<pk>\d+)$', EditProducto.as_view(), name='producto_edit'),
    url(r'^delete_producto/(?P<producto>\d+)$', 'apps.producto.views.DeleteProducto', name='delete_producto'),

	url(r'^Createcategoria/', CrearCategoria.as_view(), name='CrearCategoria'),
	url(r'^listacategoria/', ListCategoria.as_view(), name='lista_categoria'),
    url(r'^edit_categoria/(?P<pk>\d+)$', EditCategoria.as_view(), name='edit_categoria'),
    url(r'^delete_categoria/(?P<categoria>\d+)$', 'apps.producto.views.DeleteCategoria', name='categoria_delete'),



    url(r'^Createmarca/', CrearMarca.as_view(), name='CrearMarca'),
	url(r'^listamarca/', ListMarca.as_view(), name='lista_marca'),
    url(r'^edit_marca/(?P<pk>\d+)$', EditMarca.as_view(), name='edit_marca'),
    url(r'^delete_marca/(?P<marca>\d+)$', 'apps.producto.views.DeleteMarca', name='delete_marca'),

)
