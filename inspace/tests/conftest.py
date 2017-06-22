import pytest
from django.test import Client
from mixer.backend.django import mixer

from core.models import Resource


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def resources():
    titles = ['python', 'ruby', 'php']
    resources = mixer.cycle(3).blend(Resource, title=(x for x in titles))
    return Resource
