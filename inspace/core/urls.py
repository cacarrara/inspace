from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^resources/new/$', views.resource_create_view, name='resource-create'),
    url(r'^$', views.home_view, name='home'),
]
