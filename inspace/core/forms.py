from django.forms import ModelForm

from .models import Planet, Resource


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'


class PlanetForm(ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'
