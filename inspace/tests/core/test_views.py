from django.core.urlresolvers import reverse
import pytest

pytestmark = pytest.mark.django_db


def test_home_get_successfully(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200


def test_home_resouces(client, resources):
    url = reverse('core:home')
    response = client.get(url)
    assert len(response.context['resources']) == 3


def test_home_resouces_links(client, resources_links):
    url = reverse('core:home')
    response = client.get(url)
    assert len(response.context['resources_links']) == 3


def test_home_planets(client, planet):
    url = reverse('core:home')
    response = client.get(url)
    assert len(response.context['planets']) == 1


def test_resource_list_successfully(client):
    response = client.get(reverse('core:resource-list'))
    assert response.status_code == 200


def test_resources_number_all(client, resources):
    response = client.get(reverse('core:resource-list'))
    assert len(response.context['resources']) == 3


def test_resouces_query_icontains(client, resources, planet_resources):
    url = reverse('core:resource-list')
    response = client.get(url, {'title': 'inspace'})
    assert len(response.context['resources']) == 1
    planet_response = client.get(url, {'planet': 'jupiter'})
    assert len(planet_response.context['resources']) == 1


def test_resource_list_pagination(client, resource_list):
    url = reverse('core:resource-list')
    response = client.get(url, {'page': 4})
    # Test last page only has 5 resources
    assert len(response.context['resources']) == 5


def test_resource_list_nan_pagination(client, resource_list):
    url = reverse('core:resource-list')
    nan_response = client.get(url, {'page': None})
    # Test NaN page request returns first pagination page
    assert nan_response.context['resources'].number == 1


def test_resource_list_invalid_request_pagination(client, resource_list):
    url = reverse('core:resource-list')
    invalid_page_response = client.get(url, {'page': 5})
    # Test invalid page number returns last page
    assert invalid_page_response.context['resources'].number == 4


def test_resource_create_is_resource_in_context(client):
    url = reverse('core:resource-create')
    response = client.get(url)
    assert 'is_resource' in response.context


def test_resource_create_is_redirect_on_success(client, planet):
    url = reverse('core:resource-create')
    data = {
        'title': 'test_title',
        'description': 'test description',
        'planet': planet.id
    }
    response = client.post(url, data=data)
    target_url = reverse('core:resource-list') + '?title=' + data['title']
    assert response.status_code == 302
    assert response.url == target_url


def test_resource_create_has_error_when_invalid(client, planet):
    url = reverse('core:resource-link-create')
    data = {
        'planet': planet.id
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context['form'].errors


def test_resource_link_create_is_resource_link_in_context(client):
    url = reverse('core:resource-link-create')
    response = client.get(url)
    assert 'is_resource_link' in response.context


def test_resource_link_create_is_redirect_on_success(client, planet):
    url = reverse('core:resource-link-create')
    data = {
        'url': 'www.test.url',
        'title': 'test_title',
        'planet': planet.id
    }
    response = client.post(url, data=data)
    target_url = reverse('core:resource-list') + '?title=' + data['title']
    assert response.status_code == 302
    assert response.url == target_url


def test_resource_link_create_has_error_when_invalid(client, planet):
    url = reverse('core:resource-link-create')
    data = {
        'planet': planet.id
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context['form'].errors


def test_planet_create_is_redirect_on_success(client):
    url = reverse('core:planet-create')
    data = {
        'name': 'test_namek',
    }
    response = client.post(url, data=data)
    target_url = reverse('core:home')
    assert response.status_code == 302
    assert response.url == target_url


def test_planet_create_has_error_when_invalid(client):
    url = reverse('core:planet-create')
    data = {}
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context['form'].errors
