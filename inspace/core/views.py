from urllib.parse import urlencode

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView, ListView
from .forms import PlanetForm, ResourceForm
from .models import Planet, Resource


class HomeTemplateView(TemplateView):
    http_method_names = ('get', )
    template_name = 'core/home.html'


home_view = HomeTemplateView.as_view()


class ResourceCreateView(CreateView):
    template_name = 'core/resource_form.html'
    model = Resource
    form_class = ResourceForm
    context_object_name = 'resource'

    def get_success_url(self):
        return '{}?{}'.format(
            reverse('core:resource-list'),
            urlencode({'title': self.object.title}),
        )


resource_create_view = ResourceCreateView.as_view()


class ResourceListView(ListView):
    http_method_names = ('get', )
    model = Resource

    def get_queryset(self):
        title = self.request.GET.get('title')
        if title:
            return self.model.objects.filter(title__icontains=title)
        else:
            return self.model.objects.all()


resource_list_view = ResourceListView.as_view()


class PlanetCreateView(CreateView):
    model = Planet
    form_class = PlanetForm
    context_object_name = 'planet'

    def get_success_url(self):
        return reverse('core:home')


planet_create_view = PlanetCreateView.as_view()
