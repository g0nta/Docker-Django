from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tasks/$', views.index, name='index'),
]