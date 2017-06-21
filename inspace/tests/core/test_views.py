from django.core.urlresolvers import reverse
import pytest


def test_home_get_successfully(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_resource_list_successfully(client):
    response = client.get(
        reverse('core:resource-list', kwargs={'title': 'python'}))
    assert response.status_code == 200