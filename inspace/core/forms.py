from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Resource


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
        widgets = {
            'planet': TextInput()
        }
