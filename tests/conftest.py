import pytest

from inspace.provider import Provider


@pytest.fixture()
def galaxy_name():
    return 'Milky Way'


@pytest.fixture()
def provider():
    return Provider()


@pytest.fixture()
def provider_loaded(galaxy_name, provider):
    provider.create_galaxy(galaxy_name)
    return provider
