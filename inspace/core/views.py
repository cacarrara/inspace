import logging

from django.views.generic import CreateView, TemplateView, ListView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
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
    logger = logging.getLogger('django.request')

    http_method_names = ('post', )
    model = Resource
    template_name = 'core/resource_list.html'
    context_object_name = 'resource_list'

    def get_queryset(self):
        title = self.request.POST.get('title')
        # QUERY TABELA
        return self.model.objects.all()

    def post(self, request, **kwargs):
        # return self.get(self, request, **kwargs)
        return super().get(self, request, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        self.logger.warning(
            'Method Not Allowed (%s): %s', request.method, request.path,
            extra={'status_code': 405, 'request': request}
        )
        return redirect('core:home')

resource_list_view = ResourceListView.as_view()
