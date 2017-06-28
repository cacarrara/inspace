from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^planets/new/$',
        views.planet_create_view, name='planet-create'),
    url(r'^resources/new/$',
        views.resource_create_view, name='resource-create'),
    url(r'^resources/', views.resource_list_view, name='resource-list'),
    url(r'^$', views.home_view, name='home'),
]
