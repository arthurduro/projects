from django.conf.urls import patterns, include, url
from .views import ListProducto


urlpatterns = patterns('',

    # url(r'^producto', ProductoList.as_view(), name='compani'),
    # url(r'^/(?P<pk>\d+)$', ProductoDetail.as_view(), name='post-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', ProductoDetail.as_view()),
    url(r'^listaproducto/', ListProducto.as_view(), name='producto'),
)