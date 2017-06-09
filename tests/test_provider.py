import pytest

from schematics.exceptions import ModelValidationError


def test_provider_galaxy_create(galaxy_name, provider):
    galaxy = provider.create_galaxy(galaxy_name)
    assert galaxy.name == galaxy_name


def test_provider_galaxy_create_invalid(provider):
    with pytest.raises(ModelValidationError):
        provider.create_galaxy(None)


def test_provider_galaxy_create_repeated_name(galaxy_name, provider):
    first_id = provider.create_galaxy(galaxy_name).id
    second_id = provider.create_galaxy(galaxy_name).id
    assert len(provider.galaxies) == 1
    assert first_id == second_id


def test_provider_galaxy_get_by_name(galaxy_name, provider_loaded):
    galaxy = provider_loaded.get_galaxy(galaxy_name)
    assert galaxy
    assert galaxy.name == galaxy_name


def test_provider_galaxy_get_by_name_dont_created(galaxy_name, provider):
    galaxy = provider.get_galaxy(galaxy_name)
    assert galaxy is None
