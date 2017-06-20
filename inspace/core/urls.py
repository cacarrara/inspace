from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^resources/new/$',
        views.resource_create_view, name='resource-create'),
    url(r'^resources/search/$',
        views.resource_list_view, name='resource-list'),
    url(r'^$', views.home_view, name='home'),
]
