from django.conf.urls import include, url

from .views import Index, LoginView, LogoutView


urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
   	url(r'^login/$', LoginView.as_view(), name='login'),
  	url(r'^logout/$', LogoutView.as_view(), name='logout'),
  	
]
