from unittest import mock

from core.utils import get_site_description


@mock.patch('core.utils.requests.get')
def test_get_site_description(get_mocked, mocked_response):
    get_mocked.return_value = mocked_response
    url = 'www.test_url.com'
    expected = 'test description'
    assert get_site_description(url) == expected
