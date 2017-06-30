import pytest
from django.test import Client
from mixer.backend.django import mixer

from core.models import Planet, Resource


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def resources():
    titles = ['python', 'ruby', 'php']
    return mixer.cycle(3).blend(Resource, title=(x for x in titles))


@pytest.fixture
def planet():
    return mixer.blend(Planet)
