from django.core.urlresolvers import reverse


def test_home_get_successfully(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200


def test_resource_list_successfully(client):
    response = client.get(reverse('core:resource-list', {'title': 'python'}))
    assert response.status_code == 200
