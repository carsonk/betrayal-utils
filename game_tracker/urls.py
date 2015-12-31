from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^update/(?P<character_id>[0-9]+)/$', views.update_attr, name='update_attr'),
    url(r'^reset/', views.reset, name='reset'),
    url(r'^$', views.index, name='index'),
]
