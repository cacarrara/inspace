import pytest
from django.db.utils import IntegrityError
from mixer.backend.django import mixer

from core.models import Planet, Resource, ResourceLink

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


# ResourceLink should update the slug field if not provided
def test_resource_link_save_method_mixin():
    resource_link = mixer.blend(
        ResourceLink,
        url='https://www.planetexpress.com/',
        title='Planet Express',
        planet__name='Earth'
    )
    assert resource_link.slug == 'planet-express'


def test_resource_save_method_mixin():
    resource = mixer.blend(
        ResourceLink,
        title='Planet Express',
        planet__name='Earth'
    )
    assert resource.slug == 'planet-express'


def test_resource_str():
    resource = mixer.blend(Resource, title='test title')
    assert 'test title' == str(resource)


def test_resource_is_link():
    assert not mixer.blend(Resource).is_link()


def test_resource_link_uniqueness_title():
    mixer.blend(ResourceLink, title='test title', url='')
    with pytest.raises(IntegrityError):
        mixer.blend(ResourceLink, title='test title')


def test_resource_link_uniqueness_url():
    mixer.blend(ResourceLink, url='www.testurl.com')
    with pytest.raises(IntegrityError):
        mixer.blend(ResourceLink, url='www.testurl.com')


def test_resource_link_str():
    resource_link = mixer.blend(ResourceLink, url='www.testurl.com', title="test title")
    assert 'test title <www.testurl.com>' == str(resource_link)


def test_resource_link_is_link():
    assert mixer.blend(ResourceLink, url='').is_link()
