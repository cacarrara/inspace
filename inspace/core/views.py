from urllib.parse import urlencode

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView
from .forms import PlanetForm, ResourceForm, ResourceLinkForm
from .models import Planet, Resource, ResourceLink


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['is_resource'] = True
        return context


resource_create_view = ResourceCreateView.as_view()


class ResourceLinkCreateView(CreateView):
    template_name = 'core/resource_form.html'
    model = ResourceLink
    form_class = ResourceLinkForm
    context_object_name = 'resource_link'

    def get_success_url(self):
        return '{}?{}'.format(
            reverse('core:resource-list'),
            urlencode({'title': self.object.title}),
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['is_resource_link'] = True
        return context


resource_link_create_view = ResourceLinkCreateView.as_view()


class ResourcesTemplateView(TemplateView):
    template_name = 'core/resources.html'
    http_method_names = ('get', )

    def get_resource_queryset(self, title, planet):
        if title:
            qs = Resource.objects.filter(title__contains=title)
        else:
            qs = Resource.objects.all()

        if planet:
            qs = qs.filter(planet__name__icontains=planet)
        return qs

    def get_resource_link_queryset(self, title, planet):
        if title:
            qs = ResourceLink.objects.filter(title__contains=title)
        else:
            qs = ResourceLink.objects.all()

        if planet:
            qs = qs.filter(planet__name__icontains=planet)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        title = self.request.GET.get('title')
        planet = self.request.GET.get('planet')
        resource_qs = self.get_resource_queryset(title, planet)
        resource_link_qs = self.get_resource_link_queryset(title, planet)
        resources = [r for r in resource_qs]
        resources.extend([r for r in resource_link_qs])
        context['resources'] = resources
        return context


resources_view = ResourcesTemplateView.as_view()


class PlanetCreateView(CreateView):
    template_name = 'core/planet_form.html'
    model = Planet
    form_class = PlanetForm
    context_object_name = 'planet'

    def get_success_url(self):
        return reverse('core:home')


planet_create_view = PlanetCreateView.as_view()
