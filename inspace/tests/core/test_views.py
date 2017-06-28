from django.core.urlresolvers import reverse
import pytest


def test_home_get_successfully(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_resource_list_successfully(client):
    response = client.get(
        reverse('core:resource-list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_resources_number_all(client, resources):
    response = client.get(
        reverse('core:resource-list'))
    assert len(response.context['resource_list']) == 3


@pytest.mark.django_db
def test_resouces_query_icontains(client, resources):
    url = reverse('core:resource-list')
    response = client.get(url, {'title': 'p'})
    assert len(response.context['resource_list']) == 2
