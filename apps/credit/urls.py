from django.conf.urls import url
from . import views	
# Create your views here.

urlpatterns =[
	url(r'^$', views.index, name="dashboard"),
	url(r'^add$',views.add, name="add"),
	url(r'^create$', views.create, name="create"),
]