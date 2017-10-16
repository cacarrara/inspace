import pytest
from django.test import Client
from mixer.backend.django import mixer
from requests import Response

from core.models import Planet, Resource, ResourceLink


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def resources():
    titles = ['InSpace', 'ruby', 'phP']
    return mixer.cycle(3).blend(Resource, title=(x for x in titles))


@pytest.fixture
def resources_links():
    titles = ['python', 'ruby', 'php']
    return mixer.cycle(3).blend(ResourceLink, title=(x for x in titles))


@pytest.fixture
def planet():
    return mixer.blend(Planet)


@pytest.fixture
def planet_resources():
    planet_names = ['jupiter', 'venus', 'mars']
    return mixer.cycle(3).blend(
        Resource, planet__name=(n for n in planet_names)
    )


@pytest.fixture
def mocked_response_with_desc():
    mocked_response = Response()
    mocked_response._content = """
    <html lang="en">
    <head>
        <meta name='description' content='test description'>
    </head>
    <body>
    </body>
    </html>
    """
    return mocked_response


@pytest.fixture
def mocked_response_without_desc():
    mocked_response = Response()
    mocked_response._content = """
    <html lang="en">
    <head>
    </head>
    <body>
        <p>test paragraph</p>
    </body>
    </html>
    """
    return mocked_response
