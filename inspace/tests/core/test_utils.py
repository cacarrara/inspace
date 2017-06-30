from unittest import mock

from core.utils import get_site_description


@mock.patch('core.utils.requests.get')
def test_get_site_description_from_meta(get_mocked, mocked_response_with_desc):
    get_mocked.return_value = mocked_response_with_desc
    url = 'www.test_url.com'
    expected = 'test description'
    assert get_site_description(url) == expected


@mock.patch('core.utils.requests.get')
def test_get_site_description_from_paragraph(get_mocked, mocked_response_without_desc):
    get_mocked.return_value = mocked_response_without_desc
    url = 'www.test_url.com'
    expected = 'test paragraph'
    assert get_site_description(url) == expected
