import pytest
from django.test import Client
from mixer.backend.django import mixer
from requests import Response

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
