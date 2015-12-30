from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reset/', views.reset, name='reset'),
    url(r'^$', views.index, name='index'),
]
