from django.forms import ModelForm

from .models import Planet, Resource, ResourceLink


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'


class ResourceLinkForm(ModelForm):
    class Meta:
        model = ResourceLink
        fields = ('url', 'title', 'planet', )


class PlanetForm(ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'
