from django.views.generic import CreateView, TemplateView, ListView
from django.shortcuts import redirect
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


class ResourceListView(ListView):
    http_method_names = ('get', )
    model = Resource
    template_name = 'core/resource_list.html'
    context_object_name = 'resource_list'

    def get_queryset(self):
        title = self.request.GET.get('title')
        # QUERY TABELA
        return self.model.objects.all()

resource_list_view = ResourceListView.as_view()
