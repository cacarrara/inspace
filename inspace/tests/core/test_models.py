import pytest
from django.db.utils import IntegrityError
from mixer.backend.django import mixer

from core.models import Planet, Resource

pytestmark = pytest.mark.django_db


def test_planet_uniqueness():
    mixer.blend(Planet, name='test name')
    with pytest.raises(IntegrityError):
        mixer.blend(Planet, name='test name')


def test_planet_str():
    planet = mixer.blend(Planet, name='test name')
    assert 'test name' == str(planet)


def test_resource_uniqueness():
    mixer.blend(Resource, title='test title')
    with pytest.raises(IntegrityError):
        mixer.blend(Resource, title='test title')


def test_resource_str():
    resource = mixer.blend(Resource, title='test title')
    assert 'test title' == str(resource)
