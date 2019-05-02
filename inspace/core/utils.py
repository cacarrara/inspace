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
        logger.warning('Connection error trying to connect to {}'.format(url))

    if site_content:
        target_markup = BeautifulSoup(site_content, 'html.parser')
        meta_description = target_markup.head.find('meta', {'name': 'description'})
        if meta_description:
            description = meta_description.get('content')
        else:
            first_paragraph = target_markup.find('p')
            if first_paragraph:
                description = first_paragraph.string
    return description
