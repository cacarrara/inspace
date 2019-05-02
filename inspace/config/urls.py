from django.urls import include, path


urlpatterns = [
    path(r'', include('core.urls', namespace='core')),
]
