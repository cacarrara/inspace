import logging

from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException


logger = logging.getLogger(__name__)


def get_site_description(url):
    site_content = description = ''
    try:
        site_content = requests.get(url, timeout=1).content
    except RequestException:
        logger.warn('Connection error trying to connect to {}'.format(url))

    if site_content:
        target_markup = BeautifulSoup(site_content, 'html.parser')
        description = target_markup.head.find('meta', {'name': 'description'}).get('content')
    return description
