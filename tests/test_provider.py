import pytest

from schematics.exceptions import ModelValidationError


def test_provider_galaxy_get_new(galaxy_name, provider):
    galaxy = provider.get_galaxy(galaxy_name)
    assert galaxy.name == galaxy_name


def test_provider_galaxy_get_invalid(provider):
    with pytest.raises(ModelValidationError):
        provider.get_galaxy(None)


def test_provider_galaxy_get_existent(galaxy_name, provider):
    first_id = provider.get_galaxy(galaxy_name).id
    second_id = provider.get_galaxy(galaxy_name).id
    assert len(provider.galaxies) == 1
    assert first_id == second_id
