from django.urls import path

from . import views


app_name = 'core'


urlpatterns = [
    path(
        'planet/',
        views.planet_create_view,
        name='planet-create'
    ),
    path(
        'resource/',
        views.resource_create_view,
        name='resource-create'
    ),
    path(
        'resourcelink/',
        views.resource_link_create_view,
        name='resource-link-create'
    ),
    path(
        'resources/',
        views.resources_view,
        name='resource-list'
    ),
    path(
        'resource/<slug:slug>/',
        views.ResourceDetailView.as_view(),
        name='resource'
    ),
    path(
        'resource-link/<slug:slug>/',
        views.ResourceLinkDetailView.as_view(),
        name='resource-link'
    ),
    path(
        '',
        views.home_view,
        name='home'
    ),
]
