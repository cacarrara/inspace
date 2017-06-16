from django.views.generic import CreateView, TemplateView

from .forms import ResourceForm
from .models import Resource


class HomeTemplateView(TemplateView):
    http_method_names = ('get', )
    template_name = 'core/home.html'


home_view = HomeTemplateView.as_view()


class ResourceCreateView(CreateView):
    template_name = 'core/resource_form.html'
    model = Resource
    form_class = ResourceForm
    context_object_name = 'reosource'


resource_create_view = ResourceCreateView.as_view()
