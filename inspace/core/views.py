from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    http_method_names = ('get', )
    template_name = 'core/home.html'


home_view = HomeTemplateView.as_view()
